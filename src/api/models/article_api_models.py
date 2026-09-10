from typing import TypedDict


class ArticlePayload(TypedDict):
    title: str
    body: str
    date: str
    image: str
