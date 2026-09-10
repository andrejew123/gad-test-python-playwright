from typing import TypedDict


class CommentPayload(TypedDict):
    article_id: int
    body: str
    date: str
