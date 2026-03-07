#!/usr/bin/env python3
"""
PM Newsletter -> Cloud Ingestion Script

Fetches new articles from PM newsletter RSS feeds, generates AI summaries
via Claude API, and writes them as markdown notes to the repo's notes/
directory. Designed to run in GitHub Actions.

The local sync script (sync_to_vault.sh) copies these notes into the
Obsidian vault on the user's machine.
"""

import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

import anthropic
import feedparser
import httpx
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.json"
NOTES_DIR = SCRIPT_DIR / "notes"
ENV_PATH = SCRIPT_DIR / ".env"

# Load .env file if it exists (local dev; in CI, env vars are injected)
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            k, v = key.strip(), value.strip()
            if not os.environ.get(k):
                os.environ[k] = v

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger(__name__)


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)


def load_seen(seen_file: str) -> list[str]:
    path = SCRIPT_DIR / "seen" / seen_file
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []


def save_seen(seen_file: str, urls: list[str]) -> None:
    path = SCRIPT_DIR / "seen" / seen_file
    with open(path, "w") as f:
        json.dump(urls, f, indent=2)


def fetch_feed(feed_url: str) -> list[dict]:
    """Parse RSS feed and return list of article entries."""
    log.info(f"Fetching RSS feed: {feed_url}")
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        published = ""
        published_iso = ""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
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
    log.info(f"Found {len(articles)} articles in feed")
    return articles


def fetch_article_content(url: str) -> str:
    """Fetch full article page and extract text content."""
    log.info(f"Fetching article: {url}")
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        log.warning(f"Failed to fetch {url}: {e}")
        return ""

    soup = BeautifulSoup(resp.text, "html.parser")

    # Substack articles use .body.markup for main content
    content_div = soup.select_one(".body.markup") or soup.select_one("article") or soup.select_one(".post-content")
    if content_div:
        for tag in content_div.find_all(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = content_div.get_text(separator="\n", strip=True)
    else:
        text = soup.get_text(separator="\n", strip=True)

    # Truncate to ~8000 chars to stay within token limits
    if len(text) > 8000:
        text = text[:8000] + "\n[... truncated]"

    return text


def get_existing_notes() -> list[str]:
    """Scan existing notes in the repo's notes/ directory for cross-links."""
    notes = []
    if NOTES_DIR.exists():
        for md_file in NOTES_DIR.rglob("*.md"):
            notes.append(md_file.stem)
    return notes


def sanitize_filename(title: str) -> str:
    """Clean title for use as filename."""
    cleaned = re.sub(r'[<>:"/\\|?*]', "", title)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if len(cleaned) > 80:
        cleaned = cleaned[:80].rsplit(" ", 1)[0]
    return cleaned


def generate_summary(
    client: anthropic.Anthropic,
    model: str,
    feed_name: str,
    feed_author: str,
    title: str,
    content: str,
    published: str,
    existing_notes: list[str],
) -> dict:
    """Use Claude to generate a structured summary."""
    existing_list = "\n".join(f"- {n}" for n in existing_notes) if existing_notes else "None yet"

    prompt = f"""Analyze this article and return a JSON object with these fields:

1. "summary": A 1-2 sentence summary of the article's core argument.

2. "takeaways": An array of 3-5 key takeaway strings. Each should be actionable and specific. Start each with a bolded phrase.

3. "author": The default author of this feed is {feed_author}. Use this unless the article features a guest, in which case use "{feed_author} (featuring Guest Name)".

4. "related": An array of 2-3 filenames from the existing notes list below that are most related to this article. Use exact filenames.

This article is from: {feed_name}

Existing notes in the vault:
{existing_list}

Article title: {title}
Published: {published}

Article content:
{content}

Return ONLY valid JSON, no markdown fences or other text."""

    log.info(f"Generating summary for: {title}")
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    # Strip markdown fences if present
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    return json.loads(text)


def format_note(title: str, url: str, published: str, feed_name: str, result: dict) -> str:
    """Format the summary as an Obsidian markdown note."""
    lines = [
        f"# {title}",
        "",
        f"**Source**: [{feed_name}]({url})",
        f"**Author**: {result.get('author', 'Unknown')} | **Date**: {published}",
        "",
        "---",
        "",
        "## Summary",
        "",
        result.get("summary", ""),
        "",
        "## Key Takeaways",
        "",
    ]

    for takeaway in result.get("takeaways", []):
        lines.append(f"- {takeaway}")

    lines.extend(["", "## Related", ""])

    for related in result.get("related", []):
        lines.append(f"- [[{related}]]")

    return "\n".join(lines) + "\n"


def process_feed(
    feed_config: dict,
    config: dict,
    client: anthropic.Anthropic,
    existing_notes: list[str],
) -> int:
    """Process a single feed. Returns number of articles processed."""
    feed_name = feed_config["name"]
    feed_url = feed_config["url"]
    seen_file = feed_config["seen_file"]

    log.info(f"--- Processing feed: {feed_name} ---")

    seen_urls = load_seen(seen_file)
    articles = fetch_feed(feed_url)

    # Skip articles older than 30 days to avoid processing huge back-catalogs
    cutoff = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    new_articles = [
        a for a in articles
        if a["url"] not in seen_urls
        and (not a["published_iso"] or a["published_iso"] >= cutoff)
    ]

    if not new_articles:
        log.info(f"No new articles from {feed_name}")
        return 0

    log.info(f"Found {len(new_articles)} new article(s) from {feed_name}")
    processed = 0

    for article in new_articles:
        try:
            # Fetch full content
            content = fetch_article_content(article["url"])
            if not content:
                content = BeautifulSoup(article["description"], "html.parser").get_text()

            # Generate AI summary
            result = generate_summary(
                client=client,
                model=config["model"],
                feed_name=feed_name,
                feed_author=feed_config.get("author", "Unknown"),
                title=article["title"],
                content=content,
                published=article["published"],
                existing_notes=existing_notes,
            )

            # Write to notes/ directory within the repo
            feed_dir = NOTES_DIR / feed_name
            feed_dir.mkdir(parents=True, exist_ok=True)

            date_prefix = article.get("published_iso", "")
            title_part = sanitize_filename(article["title"])
            filename = f"{date_prefix} {title_part}.md" if date_prefix else f"{title_part}.md"
            note_path = feed_dir / filename

            note_content = format_note(
                title=article["title"],
                url=article["url"],
                published=article["published"],
                feed_name=feed_name,
                result=result,
            )
            note_path.write_text(note_content, encoding="utf-8")
            log.info(f"Wrote: {note_path.relative_to(SCRIPT_DIR)}")

            # Track as seen
            seen_urls.append(article["url"])
            existing_notes.append(sanitize_filename(article["title"]))
            processed += 1

        except Exception as e:
            log.error(f"Failed to process '{article['title']}': {e}")
            continue

    save_seen(seen_file, seen_urls)
    return processed


def main():
    config = load_config()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        log.error("ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic()

    feeds = config.get("feeds")
    if not feeds:
        feeds = [{
            "name": "Product Growth",
            "url": config["feed_url"],
            "seen_file": "seen_articles.json",
        }]

    # Get existing notes from the repo's notes/ directory for cross-linking
    existing_notes = get_existing_notes()

    total_processed = 0
    for feed_config in feeds:
        processed = process_feed(feed_config, config, client, existing_notes)
        total_processed += processed

    log.info(f"Done. Processed {total_processed} new article(s) across {len(feeds)} feed(s)")


if __name__ == "__main__":
    main()
