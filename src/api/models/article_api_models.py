from pydantic import BaseModel


class ArticlePayload(BaseModel):
    title: str
    body: str
    date: str
    image: str
