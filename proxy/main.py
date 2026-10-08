"""PM Pulse feed proxy: a tiny Cloud Run service that fetches RSS feeds.

Substack's bare *.substack.com domains return a Cloudflare 403 to GitHub
Actions runners, while Google Cloud egress is allowed through. feedfetch.py in
the main repo retries a blocked feed through this service.

Security model: callers must present the shared token in X-Proxy-Token, and
only hosts matching ALLOWED_HOST_SUFFIXES (default: substack.com) can be
fetched, including after redirects. Nothing is cached or stored.
"""

import hmac
import os
from urllib.parse import urlparse

import httpx
from flask import Flask, Response, abort, request

app = Flask(__name__)

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)
ACCEPT = (
    "application/rss+xml, application/atom+xml, application/xml;q=0.9, "
    "text/xml;q=0.8, text/html;q=0.7, */*;q=0.5"
)
MAX_BYTES = 5 * 1024 * 1024


def _suffixes() -> tuple[str, ...]:
    raw = os.environ.get("ALLOWED_HOST_SUFFIXES", "substack.com")
    return tuple(s.strip().lower() for s in raw.split(",") if s.strip())


def host_allowed(host: str | None) -> bool:
    if not host:
        return False
    host = host.lower()
    return any(host == s or host.endswith("." + s) for s in _suffixes())


@app.get("/")
def health():
    return "ok"


@app.get("/fetch")
def fetch():
    token = os.environ.get("PROXY_TOKEN", "")
    presented = request.headers.get("X-Proxy-Token", "")
    if not token or not hmac.compare_digest(presented, token):
        abort(401)

    url = request.args.get("url", "")
    parsed = urlparse(url)
    if parsed.scheme != "https" or not host_allowed(parsed.hostname):
        abort(403)

    try:
        upstream = httpx.get(
            url, headers={"User-Agent": UA, "Accept": ACCEPT},
            timeout=25, follow_redirects=True,
        )
    except httpx.HTTPError as e:
        return Response(f"upstream error: {e}", status=502, mimetype="text/plain")

    if not host_allowed(upstream.url.host):
        abort(403)
    body = upstream.content[:MAX_BYTES]
    return Response(
        body,
        status=upstream.status_code,
        headers={
            "Content-Type": upstream.headers.get("content-type", "application/octet-stream"),
            "X-Upstream-Status": str(upstream.status_code),
            "Cache-Control": "no-store",
        },
    )
