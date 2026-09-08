from datetime import datetime, timezone
from typing import TypedDict

from playwright.sync_api import APIRequestContext

from src.factories.articles_factory import prepare_random_article
from src.factories.comment_factory import prepare_random_comment
from src.test_data.user_data import test_user_1

API_LINKS = {
    "articles_url": "/api/articles",
    "comments_url": "/api/comments",
}


class ArticlePayload(TypedDict):
    title: str
    body: str
    date: str
    image: str


class CommentPayload(TypedDict):
    article_id: int
    body: str
    date: str


def _current_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def get_authorization_header(request: APIRequestContext) -> dict[str, str]:
    login_url = "/api/login"
    response = request.post(
        login_url,
        data={
            "email": test_user_1.user_email,
            "password": test_user_1.user_password,
        },
    )
    response_json = response.json()
    return {"Authorization": f"Bearer {response_json['access_token']}"}


def prepare_article_payload() -> ArticlePayload:
    random_article = prepare_random_article()
    return {
        "title": random_article.title,
        "body": random_article.body,
        "date": _current_utc_timestamp(),
        "image": "",
    }


def prepare_comment_payload(article_id: int) -> CommentPayload:
    random_comment = prepare_random_comment()
    return {
        "article_id": article_id,
        "body": random_comment.body,
        "date": _current_utc_timestamp(),
    }
