"""Tests for the Cloud Run feed proxy in proxy/main.py."""

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "proxy"))

import main as proxy  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("PROXY_TOKEN", "sekrit")
    monkeypatch.delenv("ALLOWED_HOST_SUFFIXES", raising=False)
    proxy.app.config["TESTING"] = True
    return proxy.app.test_client()


def _upstream(status=200, body=b"<rss/>", host="lg.substack.com"):
    r = MagicMock(status_code=status, content=body, headers={"content-type": "application/xml"})
    r.url.host = host
    return r


def test_health(client):
    assert client.get("/").data == b"ok"


def test_rejects_missing_or_wrong_token(client):
    assert client.get("/fetch?url=https://lg.substack.com/feed").status_code == 401
    assert client.get("/fetch?url=https://lg.substack.com/feed", headers={"X-Proxy-Token": "nope"}).status_code == 401


def test_rejects_disallowed_host_and_scheme(client):
    h = {"X-Proxy-Token": "sekrit"}
    assert client.get("/fetch?url=https://example.com/feed", headers=h).status_code == 403
    assert client.get("/fetch?url=http://lg.substack.com/feed", headers=h).status_code == 403
    assert client.get("/fetch?url=https://evil-substack.com/feed", headers=h).status_code == 403


@patch("main.httpx.get", return_value=_upstream())
def test_fetches_allowed_host(mock_get, client):
    r = client.get("/fetch?url=https://lg.substack.com/feed", headers={"X-Proxy-Token": "sekrit"})
    assert r.status_code == 200
    assert r.data == b"<rss/>"
    assert r.headers["Content-Type"].startswith("application/xml")
    assert mock_get.call_args.args[0] == "https://lg.substack.com/feed"
    assert "Mozilla/5.0" in mock_get.call_args.kwargs["headers"]["User-Agent"]


@patch("main.httpx.get", return_value=_upstream(host="attacker.example"))
def test_rejects_redirect_off_allowlist(mock_get, client):
    r = client.get("/fetch?url=https://lg.substack.com/feed", headers={"X-Proxy-Token": "sekrit"})
    assert r.status_code == 403


@patch("main.httpx.get", return_value=_upstream(status=403, body=b"blocked"))
def test_passes_upstream_status_through(mock_get, client):
    r = client.get("/fetch?url=https://lg.substack.com/feed", headers={"X-Proxy-Token": "sekrit"})
    assert r.status_code == 403
    assert r.headers["X-Upstream-Status"] == "403"


def test_custom_suffixes(monkeypatch):
    monkeypatch.setenv("ALLOWED_HOST_SUFFIXES", "substack.com, example.org")
    assert proxy.host_allowed("blog.example.org")
    assert proxy.host_allowed("lg.substack.com")
    assert not proxy.host_allowed("example.org.evil")
