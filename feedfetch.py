"""Shared feed fetching for ingest_cloud.py, digest_cloud.py and backfill_notes.py.

Two kinds of source are supported, selected by the feed's "type" in config.json:

- "rss" (default): an RSS or Atom feed, parsed with feedparser.
- "sitemap": an XML sitemap, for publications that have no RSS feed (beehiiv
  sites such as Growth Unhinged). Post URLs and dates come from the sitemap;
  titles come from the sitemap's <news:title> when present and otherwise from
  the page's og:title.

Downloads go through curl_cffi with Chrome impersonation when it is installed.
Substack's bare *.substack.com domains answer plain HTTP clients from
datacenter IPs (GitHub Actions runners) with a Cloudflare 403 even when the
User-Agent looks like a browser; a browser TLS fingerprint gets through.
httpx with browser-like headers is the fallback.
"""

import html
import logging
import re
from datetime import datetime, timedelta

import feedparser
import httpx

try:
    from curl_cffi import requests as _curl_requests
except ImportError:  # pragma: no cover - exercised only when the package is absent
    _curl_requests = None

log = logging.getLogger(__name__)

FEED_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "application/rss+xml, application/atom+xml, application/xml;q=0.9, "
        "text/xml;q=0.8, text/html;q=0.7, */*;q=0.5"
    ),
}

ARTICLE_PATH_MARKER = "/p/"   # beehiiv and Substack post URLs live under /p/
MAX_SITEMAP_PAGES = 20        # cap on page fetches needed to recover titles


def fetch_url(url: str, timeout: int = 30) -> tuple[int, bytes]:
    """Download a URL and return (status_code, body bytes).

    Uses curl_cffi's Chrome impersonation when available (it sets its own
    browser headers to match the TLS fingerprint), falling back to httpx.
    """
    if _curl_requests is not None:
        try:
            resp = _curl_requests.get(url, impersonate="chrome", timeout=timeout)
            return resp.status_code, resp.content
        except Exception as e:  # noqa: BLE001 - any transport error falls back
            log.warning(f"curl_cffi fetch failed for {url} ({e}); retrying with httpx")
    resp = httpx.get(url, headers=FEED_HEADERS, timeout=timeout, follow_redirects=True)
    return resp.status_code, resp.content


def parse_feed(feed_url: str):
    """Download an RSS/Atom feed and parse it with feedparser.

    Warns loudly when the feed comes back empty or with a non-200 status so a
    blocked or moved feed is visible in the logs instead of looking like
    "no new articles".
    """
    try:
        status, content = fetch_url(feed_url)
        if status != 200:
            log.warning(f"Feed {feed_url} returned HTTP {status}")
        feed = feedparser.parse(content)
    except Exception as e:  # noqa: BLE001
        log.warning(f"Feed download failed for {feed_url} ({e}); retrying via feedparser")
        feed = feedparser.parse(feed_url)

    if not feed.entries:
        reason = getattr(feed, "bozo_exception", None)
        log.warning(
            f"Feed {feed_url} returned no entries"
            + (f" ({reason})" if reason else "")
            + " - the feed may be blocked or moved"
        )
    return feed


def _rss_entries(feed_url: str) -> list[dict]:
    feed = parse_feed(feed_url)
    articles = []
    for entry in feed.entries:
        published = ""
        published_iso = ""
        if getattr(entry, "published_parsed", None):
            dt = datetime(*entry.published_parsed[:6])
            published = dt.strftime("%b %d, %Y")
            published_iso = dt.strftime("%Y-%m-%d")
        articles.append({
            "title": entry.get("title", "Untitled"),
            "url": entry.get("link", ""),
            "published": published,
            "published_iso": published_iso,
            "description": entry.get("summary", ""),
        })
    return articles


# ---------------------------------------------------------------------------
# Sitemap feeds
# ---------------------------------------------------------------------------

_URL_BLOCK_RE = re.compile(r"<url>(.*?)</url>", re.S)


def _tag(block: str, name: str) -> str:
    m = re.search(rf"<{name}>(.*?)</{name}>", block, re.S)
    return html.unescape(m.group(1).strip()) if m else ""


def _meta_content(page: str, prop: str) -> str:
    m = re.search(
        rf'<meta[^>]+(?:property|name)=["\']{re.escape(prop)}["\'][^>]+content=["\']([^"\']*)["\']',
        page, re.I,
    ) or re.search(
        rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:property|name)=["\']{re.escape(prop)}["\']',
        page, re.I,
    )
    return html.unescape(m.group(1).strip()) if m else ""


def fetch_page_title(url: str) -> tuple[str, str]:
    """Return (title, description) read from a page's og: tags or <title>."""
    try:
        status, content = fetch_url(url)
    except Exception as e:  # noqa: BLE001
        log.warning(f"Could not fetch {url} for its title ({e})")
        return "", ""
    if status != 200:
        log.warning(f"Page {url} returned HTTP {status} while fetching its title")
        return "", ""
    page = content.decode("utf-8", "replace")
    title = _meta_content(page, "og:title")
    if not title:
        m = re.search(r"<title[^>]*>(.*?)</title>", page, re.S | re.I)
        title = html.unescape(m.group(1).strip()) if m else ""
    return title, _meta_content(page, "og:description")


def slug_to_title(url: str) -> str:
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    words = slug.replace("-", " ").replace("_", " ").strip()
    return words[:1].upper() + words[1:] if words else "Untitled"


def fetch_sitemap_entries(sitemap_url: str, days: int = 30) -> list[dict]:
    """Build feed-style article dicts from an XML sitemap.

    Keeps URLs containing ARTICLE_PATH_MARKER whose date (news:publication_date,
    else lastmod) falls within the last `days` days, newest first, capped at
    MAX_SITEMAP_PAGES. lastmod can move when an old post is edited; the seen
    tracker absorbs that after the first ingest.
    """
    status, content = fetch_url(sitemap_url)
    if status != 200:
        log.warning(f"Sitemap {sitemap_url} returned HTTP {status}")
    text = content.decode("utf-8", "replace")
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    candidates = []
    for block in _URL_BLOCK_RE.findall(text):
        loc = _tag(block, "loc")
        if not loc or ARTICLE_PATH_MARKER not in loc:
            continue
        date = (_tag(block, "news:publication_date") or _tag(block, "lastmod"))[:10]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) or date < cutoff:
            continue
        candidates.append({"url": loc, "published_iso": date, "title": _tag(block, "news:title")})

    candidates.sort(key=lambda c: c["published_iso"], reverse=True)
    candidates = candidates[:MAX_SITEMAP_PAGES]

    articles = []
    for c in candidates:
        title, description = c["title"], ""
        if not title:
            title, description = fetch_page_title(c["url"])
        if not title:
            title = slug_to_title(c["url"])
        dt = datetime.strptime(c["published_iso"], "%Y-%m-%d")
        articles.append({
            "title": title,
            "url": c["url"],
            "published": dt.strftime("%b %d, %Y"),
            "published_iso": c["published_iso"],
            "description": description,
        })

    if not articles:
        log.warning(f"Sitemap {sitemap_url} yielded no article URLs in the last {days} days")
    return articles


def fetch_feed_entries(feed_url: str, feed_type: str = "rss", days: int = 30) -> list[dict]:
    """Return article dicts for a feed of either type.

    Each dict has: title, url, published ("Mar 05, 2026"), published_iso
    ("2026-03-05") and description. `days` only applies to sitemap feeds; RSS
    feeds return everything the feed carries and callers filter by date.
    """
    if feed_type == "sitemap":
        return fetch_sitemap_entries(feed_url, days=days)
    return _rss_entries(feed_url)
