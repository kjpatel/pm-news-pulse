"""Tests for digest_cloud.py utility functions."""

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from digest_cloud import (
    _deduplicate_articles,
    annotate_trending,
    build_feed_homepage_map,
    fetch_audience_contacts,
    fetch_trending_hn,
    fetch_trending_repos,
    format_digest,
    load_cached_notes,
    markdown_to_html,
    send_digest_email,
)


class TestBuildFeedHomepageMap:
    def test_strips_feed_suffix(self):
        feeds = [{"name": "Test", "url": "https://example.com/feed"}]
        result = build_feed_homepage_map(feeds)
        assert result == {"Test": "https://example.com"}

    def test_strips_index_xml(self):
        feeds = [{"name": "Blog", "url": "https://blog.com/index.xml"}]
        result = build_feed_homepage_map(feeds)
        assert result == {"Blog": "https://blog.com"}

    def test_multiple_feeds(self):
        feeds = [
            {"name": "A", "url": "https://a.com/feed"},
            {"name": "B", "url": "https://b.com/feed/"},
        ]
        result = build_feed_homepage_map(feeds)
        assert result["A"] == "https://a.com"
        assert result["B"] == "https://b.com"


class TestFormatDigest:
    def _make_articles(self, n=5):
        return [
            {
                "title": f"Article {i}",
                "url": f"https://example.com/{i}",
                "feed_name": "Test Feed",
                "author": "Author",
                "date": "Mar 01, 2026",
                "summary": f"Summary for article {i}.",
                "takeaways": [f"- Takeaway {i}"],
            }
            for i in range(n)
        ]

    def _make_ranking(self, n=5):
        return [
            {
                "index": i,
                "rank": i + 1,
                "relevance": "Relevant",
                "must_read": i < 1,
                **({"expanded_summary": f"Expanded summary for article {i}."} if i < 1 else {}),
            }
            for i in range(n)
        ]

    def test_contains_header(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "PM Pulse: Weekly Digest" in result
        assert "5 articles from 1 feeds" in result

    def test_must_read_section(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "## Must-Read" in result

    def test_must_read_uses_expanded_summary(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "Expanded summary for article 0." in result

    def test_must_read_has_why_it_matters(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "**Why it matters**:" in result

    def test_must_read_has_read_article_link(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "[Read article" in result

    def test_all_articles_listed(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        for a in articles:
            assert a["title"] in result

    def test_no_duplication(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        # Must-read article 0 should NOT appear in the "All Articles" section
        assert "**1.** [Article 0]" not in result

    def test_non_must_read_has_date(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        # Non-must-read articles should have date with · separator
        assert "· Mar 01, 2026" in result

    def test_no_feed_count_table(self):
        articles = self._make_articles()
        ranking = self._make_ranking()
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        assert "| Feed |" not in result


class TestMarkdownToHtml:
    """Tests for markdown_to_html() — digest-specific HTML email converter."""

    SAMPLE_DIGEST = (
        "# PM Pulse: Weekly Digest — Mar 07, 2026\n"
        "\n"
        "5 articles from 2 feeds | Mar 01 – Mar 07, 2026\n"
        "\n"
        "---\n"
        "\n"
        "## Must-Read\n"
        "\n"
        "### 1. [Great Article](https://example.com/1)\n"
        "*Test Feed* — Author — Mar 05, 2026\n"
        "\n"
        "This article is really good.\n"
        "\n"
        "**Why it matters**: Very relevant.\n"
        "\n"
        "- **Bold lead**: Rest of the takeaway\n"
        "\n"
        "[Read article →](https://example.com/1)\n"
        "\n"
        "---\n"
        "\n"
        "## All Articles\n"
        "\n"
        "**2.** [Another](https://example.com/2) — *Feed B* · Mar 04, 2026\n"
        "\n"
        "Summary of another article.\n"
    )

    def test_header_has_branding(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "PM Pulse" in html
        assert "NyxWorks.ai" in html

    def test_header_has_date_range(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "Mar 01" in html

    def test_must_read_section(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "Must-Read" in html

    def test_all_articles_section(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "All Articles" in html

    def test_converts_markdown_links(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert '<a href="https://example.com/1"' in html

    def test_converts_read_article_link(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "Read article" in html

    def test_converts_bold(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "<strong>" in html

    def test_wraps_in_styled_div(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert html.startswith("<div")
        assert html.endswith("</div>")

    def test_bullet_points(self):
        html = markdown_to_html(self.SAMPLE_DIGEST)
        assert "&bull;" in html


class TestLoadCachedNotes:
    def test_returns_empty_when_no_notes_dir(self, tmp_path):
        with patch("digest_cloud.NOTES_DIR", tmp_path / "nonexistent"):
            result = load_cached_notes()
            assert result == {}

    def test_loads_valid_note(self, tmp_path):
        feed_dir = tmp_path / "Test Feed"
        feed_dir.mkdir(parents=True)

        note = """# Test Article

**Source**: [Test Feed](https://example.com/1)
**Author**: Author Name | **Date**: Mar 01, 2026

---

## Summary

This is the summary.

## Key Takeaways

- **Bold** takeaway one
- **Bold** takeaway two

## Related

- [[Note A]]
"""
        (feed_dir / "2099-01-01 Test Article.md").write_text(note)

        with patch("digest_cloud.NOTES_DIR", tmp_path):
            result = load_cached_notes(days=7)

        assert "Test Article" in result
        assert result["Test Article"]["summary"] == "This is the summary."
        assert len(result["Test Article"]["takeaways"]) == 2

    def test_skips_digest_directory(self, tmp_path):
        digest_dir = tmp_path / "Digests"
        digest_dir.mkdir()
        (digest_dir / "2026-03-05 Weekly PM Digest.md").write_text("# Digest\n\n## Summary\n\nStuff")

        with patch("digest_cloud.NOTES_DIR", tmp_path):
            result = load_cached_notes(days=7)

        assert len(result) == 0


class TestDeduplicateArticles:
    def _article(self, title, url="https://example.com/a"):
        return {"title": title, "url": url, "feed_name": "Feed", "summary": "S"}

    def test_exact_duplicates_kept_once(self):
        articles = [self._article("Same Title"), self._article("Same Title")]
        result = _deduplicate_articles(articles)
        assert len(result) == 1

    def test_unique_articles_all_kept(self):
        articles = [
            self._article("Alpha Article"),
            self._article("Beta Article"),
            self._article("Gamma Article"),
        ]
        result = _deduplicate_articles(articles)
        assert len(result) == 3

    def test_podcast_wrapper_keeps_article(self):
        articles = [
            self._article("🎙️ Podcast: Building Great Products With AI and Strategy"),
            self._article("Building Great Products With AI and Strategy"),
        ]
        result = _deduplicate_articles(articles)
        assert len(result) == 1
        assert result[0]["title"] == "Building Great Products With AI and Strategy"

    def test_short_common_substring_no_dedup(self):
        # "AI" is too short relative to the full titles → no dedup
        articles = [
            self._article("The Future of AI in Enterprise Software"),
            self._article("AI Ethics and Governance Framework"),
        ]
        result = _deduplicate_articles(articles)
        assert len(result) == 2

    def test_emoji_stripped_for_comparison(self):
        articles = [
            self._article("🚀 Launch Strategy Guide"),
            self._article("Launch Strategy Guide"),
        ]
        result = _deduplicate_articles(articles)
        assert len(result) == 1


class TestSendDigestEmail:
    BASIC_CONFIG = {
        "digest_email": {
            "enabled": True,
            "from": "Test <test@example.com>",
            "to": ["alice@example.com"],
            "signup_api_url": "https://api.example.com/",
            "signup_page_url": "https://example.com/signup",
        }
    }

    def test_skip_audience_true_does_not_fetch_contacts(self):
        """Bug #1: --to flag should skip audience fetch."""
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.resend") as mock_resend,
            patch("digest_cloud.fetch_audience_contacts") as mock_fetch,
            patch("digest_cloud.markdown_to_html", return_value="<html>{{unsub_url}}{{signup_url}}</html>"),
        ):
            send_digest_email(
                self.BASIC_CONFIG, "# Digest", "Mar 01 – Mar 07",
                skip_audience=True,
            )
            mock_fetch.assert_not_called()
            mock_resend.Emails.send.assert_called_once()

    def test_skip_audience_false_fetches_and_merges(self):
        config = {
            "digest_email": {
                "enabled": True,
                "from": "Test <test@example.com>",
                "to": ["alice@example.com"],
                "resend_audience_id": "aud-123",
                "signup_api_url": "https://api.example.com/",
            }
        }
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.resend") as mock_resend,
            patch("digest_cloud.fetch_audience_contacts", return_value=["bob@example.com"]),
            patch("digest_cloud.markdown_to_html", return_value="<html></html>"),
            patch("digest_cloud.time"),
        ):
            send_digest_email(config, "# Digest", "Mar 01 – Mar 07")
            assert mock_resend.Emails.send.call_count == 2

    def test_deduplicates_config_and_audience_overlap(self):
        config = {
            "digest_email": {
                "enabled": True,
                "from": "Test <test@example.com>",
                "to": ["alice@example.com"],
                "resend_audience_id": "aud-123",
                "signup_api_url": "",
            }
        }
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.resend") as mock_resend,
            patch("digest_cloud.fetch_audience_contacts", return_value=["Alice@example.com"]),
            patch("digest_cloud.markdown_to_html", return_value="<html></html>"),
        ):
            send_digest_email(config, "# Digest", "Mar 01 – Mar 07")
            # Same email (case-insensitive) → only 1 send
            assert mock_resend.Emails.send.call_count == 1

    def test_replaces_unsub_and_signup_placeholders(self):
        """Bug #2: Footer links must be personalized per recipient."""
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.resend") as mock_resend,
            patch("digest_cloud.markdown_to_html", return_value="<a href='{{unsub_url}}'>unsub</a><a href='{{signup_url}}'>signup</a>"),
        ):
            send_digest_email(
                self.BASIC_CONFIG, "# Digest", "Mar 01 – Mar 07",
                skip_audience=True,
            )
            sent_html = mock_resend.Emails.send.call_args[0][0]["html"]
            assert "{{unsub_url}}" not in sent_html
            assert "{{signup_url}}" not in sent_html
            assert "?unsub=alice@example.com" in sent_html
            assert "https://example.com/signup" in sent_html

    def test_disabled_in_config_returns_early(self):
        config = {"digest_email": {"enabled": False}}
        with patch("digest_cloud.resend") as mock_resend:
            send_digest_email(config, "# Digest", "Mar 01 – Mar 07")
            mock_resend.Emails.send.assert_not_called()

    def test_no_api_key_returns_early(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("digest_cloud.resend") as mock_resend,
        ):
            send_digest_email(self.BASIC_CONFIG, "# Digest", "Mar 01 – Mar 07")
            mock_resend.Emails.send.assert_not_called()

    def test_no_recipients_sends_nothing(self):
        config = {
            "digest_email": {
                "enabled": True,
                "from": "Test <test@example.com>",
                "to": [],
            }
        }
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.resend") as mock_resend,
            patch("digest_cloud.markdown_to_html", return_value="<html></html>"),
        ):
            send_digest_email(config, "# Digest", "Mar 01 – Mar 07", skip_audience=True)
            mock_resend.Emails.send.assert_not_called()


class TestFetchAudienceContacts:
    def test_returns_non_unsubscribed_contacts(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "data": [
                {"email": "active@example.com", "unsubscribed": False},
                {"email": "gone@example.com", "unsubscribed": True},
            ],
        }
        mock_response.raise_for_status = MagicMock()
        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.httpx.get", return_value=mock_response),
        ):
            result = fetch_audience_contacts("aud-123")
            assert result == ["active@example.com"]

    def test_handles_pagination(self):
        page1 = MagicMock()
        page1.json.return_value = {
            "data": [{"email": "a@example.com", "unsubscribed": False}],
            "next": "cursor-abc",
        }
        page1.raise_for_status = MagicMock()

        page2 = MagicMock()
        page2.json.return_value = {
            "data": [{"email": "b@example.com", "unsubscribed": False}],
        }
        page2.raise_for_status = MagicMock()

        with (
            patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}),
            patch("digest_cloud.httpx.get", side_effect=[page1, page2]),
        ):
            result = fetch_audience_contacts("aud-123")
            assert result == ["a@example.com", "b@example.com"]

    def test_returns_empty_without_api_key(self):
        with patch.dict(os.environ, {}, clear=True):
            result = fetch_audience_contacts("aud-123")
            assert result == []

    def test_returns_empty_without_audience_id(self):
        with patch.dict(os.environ, {"RESEND_API_KEY": "test-key"}):
            result = fetch_audience_contacts("")
            assert result == []


class TestMarkdownToHtmlFooter:
    """Test that the HTML email footer contains required placeholders."""

    def _digest_md(self):
        return (
            "# PM Pulse: Weekly Digest — Mar 07, 2026\n\n"
            "5 articles from 3 feeds | Mar 01 – Mar 07, 2026\n\n"
            "---\n\n## All Articles\n\n"
            "**1.** [Test](https://example.com) — *Feed* · Mar 01, 2026\n\n"
            "Summary text.\n"
        )

    def test_footer_contains_unsub_placeholder(self):
        html = markdown_to_html(self._digest_md())
        assert "{{unsub_url}}" in html

    def test_footer_contains_signup_placeholder(self):
        html = markdown_to_html(self._digest_md())
        assert "{{signup_url}}" in html

    def test_footer_contains_forwarded_cta(self):
        html = markdown_to_html(self._digest_md())
        assert "Got forwarded this email?" in html


class TestFormatDigestWeeklyOverview:
    def _make_articles(self, n=3):
        return [
            {
                "title": f"Article {i}",
                "url": f"https://example.com/{i}",
                "feed_name": "Feed",
                "author": "Author",
                "date": "Mar 01, 2026",
                "summary": f"Summary {i}.",
                "takeaways": [],
            }
            for i in range(n)
        ]

    def _make_ranking_dict(self, n=3):
        return {
            "weekly_headline": "AI is eating product management",
            "weekly_overview": "This week saw a surge in articles about AI tools for PMs.",
            "weekly_themes": [
                "AI-powered product discovery",
                "The role of PMs in an AI world",
            ],
            "articles": [
                {"index": i, "rank": i + 1, "relevance": "R", "must_read": i < 1}
                for i in range(n)
            ],
        }

    def test_weekly_headline_rendered(self):
        result = format_digest(
            self._make_articles(), self._make_ranking_dict(),
            "Feb 28", "Mar 07, 2026",
        )
        assert "AI is eating product management" in result

    def test_weekly_overview_rendered(self):
        result = format_digest(
            self._make_articles(), self._make_ranking_dict(),
            "Feb 28", "Mar 07, 2026",
        )
        assert "This week saw a surge" in result

    def test_weekly_themes_rendered(self):
        result = format_digest(
            self._make_articles(), self._make_ranking_dict(),
            "Feb 28", "Mar 07, 2026",
        )
        assert "AI-powered product discovery" in result
        assert "The role of PMs in an AI world" in result

    def test_fallback_when_overview_missing(self):
        ranking = {
            "articles": [
                {"index": 0, "rank": 1, "relevance": "R", "must_read": False},
            ],
        }
        articles = self._make_articles(1)
        result = format_digest(articles, ranking, "Feb 28", "Mar 07, 2026")
        # Should not crash, and should not have "This Week" section
        assert "## This Week" not in result
        assert "Article 0" in result

    def test_legacy_list_format_still_works(self):
        articles = self._make_articles()
        ranking_list = [
            {"index": i, "rank": i + 1, "relevance": "R", "must_read": False}
            for i in range(3)
        ]
        result = format_digest(articles, ranking_list, "Feb 28", "Mar 07, 2026")
        assert "Article 0" in result
        assert "## This Week" not in result


class TestFetchTrendingRepos:
    SAMPLE_RESPONSE = {
        "items": [
            {
                "full_name": "owner/cool-repo",
                "html_url": "https://github.com/owner/cool-repo",
                "description": "A cool project",
                "stargazers_count": 1234,
                "language": "Python",
                "forks_count": 56,
            },
            {
                "full_name": "org/another-repo",
                "html_url": "https://github.com/org/another-repo",
                "description": None,
                "stargazers_count": 789,
                "language": None,
                "forks_count": 12,
            },
        ],
    }

    def test_returns_repos_from_api(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            repos = fetch_trending_repos(days=7, limit=5)
        assert len(repos) == 2
        assert repos[0]["name"] == "owner/cool-repo"
        assert repos[0]["stars"] == 1234
        assert repos[0]["language"] == "Python"

    def test_null_description_fallback(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            repos = fetch_trending_repos(days=7, limit=5)
        assert repos[1]["description"] == "No description"

    def test_null_language_fallback(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            repos = fetch_trending_repos(days=7, limit=5)
        assert repos[1]["language"] == "N/A"

    def test_returns_empty_on_http_error(self):
        import httpx as _httpx
        with patch("digest_cloud.httpx.get", side_effect=_httpx.HTTPError("timeout")):
            repos = fetch_trending_repos()
        assert repos == []

    def test_uses_github_token_if_available(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"items": []}
        mock_resp.raise_for_status = MagicMock()
        with (
            patch.dict(os.environ, {"GITHUB_TOKEN": "ghp_test123"}),
            patch("digest_cloud.httpx.get", return_value=mock_resp) as mock_get,
        ):
            fetch_trending_repos()
            headers = mock_get.call_args[1]["headers"]
            assert headers["Authorization"] == "Bearer ghp_test123"


class TestFormatDigestTrendingRepos:
    def _make_articles(self, n=2):
        return [
            {
                "title": f"Article {i}",
                "url": f"https://example.com/{i}",
                "feed_name": "Feed",
                "author": "Author",
                "date": "Mar 01, 2026",
                "summary": f"Summary {i}.",
                "takeaways": [],
            }
            for i in range(n)
        ]

    def _make_ranking(self, n=2):
        return {
            "articles": [
                {"index": i, "rank": i + 1, "relevance": "R", "must_read": False}
                for i in range(n)
            ],
        }

    def _make_repos(self):
        return [
            {
                "name": "owner/trending-repo",
                "url": "https://github.com/owner/trending-repo",
                "description": "A trending project",
                "stars": 5000,
                "language": "Rust",
                "forks": 100,
                "blurb": "Signals growing demand for Rust tooling in production.",
            },
        ]

    def test_trending_section_rendered(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_repos=self._make_repos(),
        )
        assert "## Trending on GitHub" in result
        assert "owner/trending-repo" in result

    def test_trending_section_omitted_when_empty(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_repos=[],
        )
        assert "Trending on GitHub" not in result

    def test_trending_section_omitted_when_none(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
        )
        assert "Trending on GitHub" not in result

    def test_trending_repo_has_stars_and_language(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_repos=self._make_repos(),
        )
        assert "5,000" in result
        assert "Rust" in result

    def test_trending_repo_has_blurb(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_repos=self._make_repos(),
        )
        assert "Signals growing demand" in result

    def test_trending_repo_without_blurb(self):
        repos = self._make_repos()
        del repos[0]["blurb"]
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_repos=repos,
        )
        assert "## Trending on GitHub" in result
        assert "owner/trending-repo" in result


class TestMarkdownToHtmlTrendingRepos:
    DIGEST_WITH_TRENDING = (
        "# PM Pulse: Weekly Digest — Mar 07, 2026\n"
        "\n"
        "5 articles from 2 feeds | Mar 01 – Mar 07, 2026\n"
        "\n"
        "---\n"
        "\n"
        "## All Articles\n"
        "\n"
        "**1.** [Test](https://example.com) — *Feed* · Mar 01, 2026\n"
        "\n"
        "Summary text.\n"
        "\n"
        "## Trending on GitHub\n"
        "\n"
        "**[owner/cool-repo](https://github.com/owner/cool-repo)** (⭐ 1,234 · Python)\n"
        "A cool project\n"
        "*Signals a shift toward AI-native dev tooling.*\n"
        "\n"
        "**[org/another](https://github.com/org/another)** (⭐ 789 · Rust)\n"
        "Another project\n"
    )

    def test_trending_section_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_TRENDING)
        assert "Trending on GitHub" in html

    def test_trending_repo_links_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_TRENDING)
        assert "github.com/owner/cool-repo" in html
        assert "github.com/org/another" in html

    def test_trending_repo_blurb_styled(self):
        html = markdown_to_html(self.DIGEST_WITH_TRENDING)
        assert "Signals a shift" in html
        assert "font-style:italic" in html

    def test_trending_repo_links_dark_grey(self):
        html = markdown_to_html(self.DIGEST_WITH_TRENDING)
        assert 'color:#333' in html

    def test_trending_repo_description_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_TRENDING)
        assert "A cool project" in html


class TestFetchTrendingHN:
    SAMPLE_RESPONSE = {
        "hits": [
            {
                "objectID": "12345",
                "title": "Show HN: Cool Project",
                "url": "https://coolproject.com",
                "points": 500,
                "num_comments": 120,
            },
            {
                "objectID": "67890",
                "title": "Ask HN: Self-post question",
                "url": None,
                "points": 300,
                "num_comments": 80,
            },
        ],
    }

    def test_returns_stories_from_api(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            stories = fetch_trending_hn(days=7, limit=5)
        assert len(stories) == 2
        assert stories[0]["title"] == "Show HN: Cool Project"
        assert stories[0]["score"] == 500
        assert stories[0]["comments"] == 120
        assert stories[0]["url"] == "https://coolproject.com"

    def test_null_url_falls_back_to_hn_link(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            stories = fetch_trending_hn(days=7, limit=5)
        assert "news.ycombinator.com/item?id=67890" in stories[1]["url"]

    def test_hn_url_always_set(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = self.SAMPLE_RESPONSE
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp):
            stories = fetch_trending_hn(days=7, limit=5)
        for story in stories:
            assert "news.ycombinator.com/item?id=" in story["hn_url"]

    def test_returns_empty_on_http_error(self):
        import httpx as _httpx
        with patch("digest_cloud.httpx.get", side_effect=_httpx.HTTPError("timeout")):
            stories = fetch_trending_hn()
        assert stories == []

    def test_passes_date_filter(self):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"hits": []}
        mock_resp.raise_for_status = MagicMock()
        with patch("digest_cloud.httpx.get", return_value=mock_resp) as mock_get:
            fetch_trending_hn(days=7, limit=5)
            params = mock_get.call_args[1]["params"]
            assert params["tags"] == "story"
            assert "created_at_i>" in params["numericFilters"]


class TestFormatDigestTrendingHN:
    def _make_articles(self, n=2):
        return [
            {
                "title": f"Article {i}",
                "url": f"https://example.com/{i}",
                "feed_name": "Feed",
                "author": "Author",
                "date": "Mar 01, 2026",
                "summary": f"Summary {i}.",
                "takeaways": [],
            }
            for i in range(n)
        ]

    def _make_ranking(self, n=2):
        return {
            "articles": [
                {"index": i, "rank": i + 1, "relevance": "R", "must_read": False}
                for i in range(n)
            ],
        }

    def _make_hn_stories(self):
        return [
            {
                "title": "Show HN: Cool Thing",
                "url": "https://cool.com",
                "score": 500,
                "comments": 120,
                "hn_url": "https://news.ycombinator.com/item?id=12345",
                "blurb": "Developer tools momentum continues to accelerate.",
            },
        ]

    def test_hn_section_rendered(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_hn=self._make_hn_stories(),
        )
        assert "## Trending on Hacker News" in result
        assert "Show HN: Cool Thing" in result

    def test_hn_section_omitted_when_empty(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_hn=[],
        )
        assert "Trending on Hacker News" not in result

    def test_hn_section_omitted_when_none(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
        )
        assert "Trending on Hacker News" not in result

    def test_hn_story_has_score_and_comments(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_hn=self._make_hn_stories(),
        )
        assert "500" in result
        assert "120" in result

    def test_hn_story_has_discussion_link(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_hn=self._make_hn_stories(),
        )
        assert "[discussion]" in result
        assert "news.ycombinator.com" in result

    def test_hn_story_has_blurb(self):
        result = format_digest(
            self._make_articles(), self._make_ranking(),
            "Feb 28", "Mar 07, 2026",
            trending_hn=self._make_hn_stories(),
        )
        assert "Developer tools momentum" in result


class TestMarkdownToHtmlTrendingHN:
    DIGEST_WITH_HN = (
        "# PM Pulse: Weekly Digest — Mar 07, 2026\n"
        "\n"
        "5 articles from 2 feeds | Mar 01 – Mar 07, 2026\n"
        "\n"
        "---\n"
        "\n"
        "## All Articles\n"
        "\n"
        "**1.** [Test](https://example.com) — *Feed* · Mar 01, 2026\n"
        "\n"
        "Summary text.\n"
        "\n"
        "## Trending on Hacker News\n"
        "\n"
        "**[Show HN: Cool Thing](https://cool.com)** (▲ 500 · 💬 120) — [discussion](https://news.ycombinator.com/item?id=12345)\n"
        "*Dev tools momentum continues to accelerate.*\n"
    )

    def test_hn_section_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_HN)
        assert "Trending on Hacker News" in html

    def test_hn_section_header_is_orange(self):
        html = markdown_to_html(self.DIGEST_WITH_HN)
        assert "#FF6600" in html

    def test_hn_story_links_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_HN)
        assert "cool.com" in html
        assert "news.ycombinator.com" in html

    def test_hn_links_orange(self):
        html = markdown_to_html(self.DIGEST_WITH_HN)
        assert 'color:#FF6600' in html

    def test_hn_blurb_styled_in_html(self):
        html = markdown_to_html(self.DIGEST_WITH_HN)
        assert "Dev tools momentum" in html
        assert "font-style:italic" in html


class TestAnnotateTrending:
    def test_adds_blurbs_to_repos_and_stories(self):
        repos = [{"name": "owner/repo", "description": "A tool", "stars": 100, "language": "Python"}]
        stories = [{"title": "Cool Post", "score": 500, "comments": 120}]

        mock_resp = MagicMock()
        mock_resp.content = [MagicMock(text='{"repos": ["Great for PMs building AI products."], "hn_stories": ["Signals a shift in dev tooling."]}')]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_resp

        annotate_trending(mock_client, "test-model", repos, stories)
        assert repos[0]["blurb"] == "Great for PMs building AI products."
        assert stories[0]["blurb"] == "Signals a shift in dev tooling."

    def test_handles_api_failure_gracefully(self):
        repos = [{"name": "owner/repo", "description": "A tool", "stars": 100, "language": "Python"}]

        mock_client = MagicMock()
        mock_client.messages.create.side_effect = Exception("API error")

        annotate_trending(mock_client, "test-model", repos, [])
        assert "blurb" not in repos[0]

    def test_skips_when_both_empty(self):
        mock_client = MagicMock()
        annotate_trending(mock_client, "test-model", [], [])
        mock_client.messages.create.assert_not_called()
