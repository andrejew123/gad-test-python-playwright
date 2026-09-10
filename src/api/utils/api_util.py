from datetime import datetime, timezone

API_LINKS = {
    "articles_url": "/api/articles",
    "comments_url": "/api/comments",
}


def _current_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
