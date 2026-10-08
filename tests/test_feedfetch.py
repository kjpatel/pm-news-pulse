"""Tests for feedfetch.py (shared RSS and sitemap fetching)."""

import sys
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

import feedfetch
from feedfetch import (
    fetch_feed_entries,
    fetch_sitemap_entries,
    fetch_url,
    parse_feed,
    slug_to_title,
)

RSS = b"""<?xml version="1.0"?><rss version="2.0"><channel><title>T</title>
<item><title>Post One</title><link>https://example.com/1</link>
<pubDate>Mon, 05 Oct 2026 10:00:00 GMT</pubDate><description>Desc</description></item></channel></rss>"""


def _recent(days_ago):
    return (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")


class TestFetchUrl:
    @patch("feedfetch.httpx.get")
    def test_uses_curl_cffi_when_available(self, mock_httpx):
        fake = MagicMock()
        fake.get.return_value = MagicMock(status_code=200, content=b"body")
        with patch("feedfetch._curl_requests", fake):
            assert fetch_url("https://lg.substack.com/feed") == (200, b"body")
        assert fake.get.call_args.kwargs["impersonate"] == "chrome"
        mock_httpx.assert_not_called()

    @patch("feedfetch.httpx.get")
    def test_falls_back_to_httpx_when_curl_cffi_fails(self, mock_httpx):
        fake = MagicMock(); fake.get.side_effect = RuntimeError("tls")
        mock_httpx.return_value = MagicMock(status_code=200, content=b"ok")
        with patch("feedfetch._curl_requests", fake):
            assert fetch_url("https://x.com/feed") == (200, b"ok")
        kwargs = mock_httpx.call_args.kwargs
        assert "Mozilla/5.0" in kwargs["headers"]["User-Agent"]
        assert kwargs["follow_redirects"] is True

    @patch("feedfetch.httpx.get")
    def test_uses_httpx_when_curl_cffi_missing(self, mock_httpx):
        mock_httpx.return_value = MagicMock(status_code=200, content=b"ok")
        with patch("feedfetch._curl_requests", None):
            assert fetch_url("https://x.com/feed") == (200, b"ok")


class TestParseFeed:
    @patch("feedfetch.fetch_url", return_value=(200, RSS))
    def test_parses_downloaded_bytes(self, _):
        feed = parse_feed("https://lg.substack.com/feed")
        assert [e.title for e in feed.entries] == ["Post One"]

    @patch("feedfetch.feedparser.parse")
    @patch("feedfetch.fetch_url", side_effect=RuntimeError("boom"))
    def test_falls_back_to_feedparser_url_on_error(self, _, mock_parse):
        mock_parse.return_value = MagicMock(entries=[1])
        feed = parse_feed("https://example.com/feed")
        mock_parse.assert_called_once_with("https://example.com/feed")
        assert feed.entries == [1]

    @patch("feedfetch.fetch_url", return_value=(403, b"<html>blocked</html>"))
    def test_warns_on_blocked_feed(self, _, caplog):
        with caplog.at_level("WARNING"):
            feed = parse_feed("https://blocked.example.com/feed")
        assert feed.entries == []
        assert "HTTP 403" in caplog.text
        assert "returned no entries" in caplog.text


class TestRssEntries:
    @patch("feedfetch.fetch_url", return_value=(200, RSS))
    def test_entry_shape(self, _):
        [a] = fetch_feed_entries("https://example.com/feed")
        assert a == {
            "title": "Post One", "url": "https://example.com/1",
            "published": "Oct 05, 2026", "published_iso": "2026-10-05",
            "description": "Desc",
        }


class TestSitemapEntries:
    def _sitemap(self):
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url><loc>https://www.growthunhinged.com/about</loc><lastmod>{_recent(1)}</lastmod></url>
  <url><loc>https://www.growthunhinged.com/p/usage-based-pricing</loc><lastmod>{_recent(1)}</lastmod>
    <news:news><news:publication_date>{_recent(2)}T10:50:00Z</news:publication_date><news:title>The AI monetization debate &amp; more</news:title></news:news></url>
  <url><loc>https://www.growthunhinged.com/p/the-30-day-upsell-window</loc><lastmod>{_recent(5)}</lastmod></url>
  <url><loc>https://www.growthunhinged.com/p/ancient-post</loc><lastmod>{_recent(200)}</lastmod></url>
  <url><loc>https://www.growthunhinged.com/p/no-date</loc></url>
</urlset>""".encode()

    def _fetch(self, url, timeout=30):
        if url.endswith("sitemap.xml"):
            return 200, self._sitemap()
        if url.endswith("the-30-day-upsell-window"):
            return 200, b'<html><head><meta property="og:title" content="The 30-Day Upsell Window" /><meta property="og:description" content="Why expansion happens early"><title>ignored</title></head></html>'
        return 404, b""

    def test_filters_titles_and_dates(self):
        with patch("feedfetch.fetch_url", side_effect=self._fetch):
            articles = fetch_sitemap_entries("https://www.growthunhinged.com/sitemap.xml", days=30)
        assert [a["url"] for a in articles] == [
            "https://www.growthunhinged.com/p/usage-based-pricing",
            "https://www.growthunhinged.com/p/the-30-day-upsell-window",
        ]
        first, second = articles
        # news:title and news:publication_date win over page fetch and lastmod
        assert first["title"] == "The AI monetization debate & more"
        assert first["published_iso"] == _recent(2)
        assert first["description"] == ""
        # no news:title -> og:title and og:description from the page
        assert second["title"] == "The 30-Day Upsell Window"
        assert second["description"] == "Why expansion happens early"
        assert second["published_iso"] == _recent(5)
        assert second["published"] == datetime.strptime(_recent(5), "%Y-%m-%d").strftime("%b %d, %Y")

    def test_slug_fallback_when_page_unavailable(self):
        sm = f'<urlset><url><loc>https://x.com/p/why-pricing-matters</loc><lastmod>{_recent(3)}</lastmod></url></urlset>'.encode()
        with patch("feedfetch.fetch_url", side_effect=lambda url, timeout=30: (200, sm) if "sitemap" in url else (500, b"")):
            [a] = fetch_sitemap_entries("https://x.com/sitemap.xml")
        assert a["title"] == "Why pricing matters"

    def test_caps_page_fetches(self):
        blocks = "".join(f"<url><loc>https://x.com/p/post-{i}</loc><lastmod>{_recent(1)}</lastmod></url>" for i in range(40))
        sm = f"<urlset>{blocks}</urlset>".encode()
        calls = []
        def fake(url, timeout=30):
            calls.append(url)
            return (200, sm) if "sitemap" in url else (404, b"")
        with patch("feedfetch.fetch_url", side_effect=fake), patch("feedfetch.MAX_SITEMAP_PAGES", 5):
            articles = fetch_sitemap_entries("https://x.com/sitemap.xml")
        assert len(articles) == 5
        assert len(calls) == 6  # sitemap + 5 pages

    def test_fetch_feed_entries_dispatches_on_type(self):
        with patch("feedfetch.fetch_sitemap_entries", return_value=["s"]) as sm, \
             patch("feedfetch._rss_entries", return_value=["r"]) as rss:
            assert fetch_feed_entries("u", "sitemap", days=7) == ["s"]
            sm.assert_called_once_with("u", days=7)
            assert fetch_feed_entries("u") == ["r"]
            rss.assert_called_once_with("u")

    def test_warns_when_empty(self, caplog):
        with patch("feedfetch.fetch_url", return_value=(200, b"<urlset></urlset>")), caplog.at_level("WARNING"):
            assert fetch_sitemap_entries("https://x.com/sitemap.xml") == []
        assert "yielded no article URLs" in caplog.text


def test_slug_to_title():
    assert slug_to_title("https://x.com/p/the-new-battleground-in-gtm/") == "The new battleground in gtm"
    assert slug_to_title("") == "Untitled"
