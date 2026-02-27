# PM Newsletter Auto-Ingest

Automatically fetches new articles from PM newsletters, generates AI-powered summaries using Claude, and writes them as organized notes to your Obsidian vault.

Built for product managers who want to stay on top of industry content without the manual effort of reading, summarizing, and filing every article.

## What It Does

```
RSS Feed → Fetch Article → Claude AI Summary → Obsidian Note
```

1. Parses RSS feeds from configured newsletters (Substack-compatible)
2. Detects new articles by comparing against a per-feed seen tracker
3. Fetches the full article content
4. Calls Claude Haiku to generate a structured summary, auto-categorize, and suggest cross-links to existing notes
5. Writes a formatted markdown note to the appropriate Obsidian vault folder
6. Tracks processed articles to prevent duplicates

## Example Output

```markdown
# How to Price AI Products: The Complete Guide for PMs

**Source**: [Product Growth](https://www.news.aakashg.com/p/how-to-price-ai-products)
**Author**: Aakash Gupta & Moe Ali | **Date**: Feb 26, 2026

---

## Summary

A comprehensive breakdown of 6 pricing models for AI products...

## Key Takeaways

- **Six pricing models**: Hybrid tiered subscriptions, usage-based...
- **Your best users are your most expensive users** — every AI interaction...

## Related

- [[AI Evals Explained Simply]]
- [[PM OS for PMs]]
```

## Setup

### Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/)
- An Obsidian vault

### Install

```bash
git clone https://github.com/kjpatel/pm-newsletter-ingest.git
cd pm-newsletter-ingest

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure

1. Copy and edit the environment file:

```bash
cp .env.example .env
# Add your Anthropic API key
```

2. Edit `config.json` to point to your vault:

```json
{
  "vault_path": "/path/to/your/obsidian/vault",
  "case_studies_path": "PM Craft/Case Studies",
  "categories": ["AI PM", "AI Update", "Getting a PM Job", "Product Growth Podcast", "Lenny's Podcast"],
  "model": "claude-haiku-4-5-20251001",
  "feeds": [
    {
      "name": "Product Growth",
      "url": "https://www.news.aakashg.com/feed",
      "seen_file": "seen_product_growth.json"
    }
  ]
}
```

### Run

```bash
source .venv/bin/activate
python3 ingest.py
```

## Adding Feeds

Add any Substack newsletter (or any RSS feed) to `config.json`:

```json
{
  "name": "Newsletter Name",
  "url": "https://example.com/feed",
  "seen_file": "seen_newsletter_name.json"
}
```

You can also add new categories to the `categories` array — the script auto-creates folders as needed.

## Scheduling (macOS)

Create a launchd plist at `~/Library/LaunchAgents/com.newsletter-ingest.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.newsletter-ingest</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/pm-newsletter-ingest/.venv/bin/python3</string>
        <string>/path/to/pm-newsletter-ingest/ingest.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/pm-newsletter-ingest/logs/ingest.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/pm-newsletter-ingest/logs/ingest-error.log</string>
</dict>
</plist>
```

Then load it:

```bash
launchctl load ~/Library/LaunchAgents/com.newsletter-ingest.plist
```

## Scheduling (Linux/cron)

```bash
crontab -e
# Add:
0 8 * * * cd /path/to/pm-newsletter-ingest && .venv/bin/python3 ingest.py >> logs/ingest.log 2>&1
```

## Cost

Uses Claude Haiku (~$0.01-0.03 per article). A typical run processing 2-3 new articles costs under $0.10.

## License

[MIT](LICENSE)
