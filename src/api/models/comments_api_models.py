from pydantic import BaseModel


class CommentPayload(BaseModel):
    article_id: int
    body: str
    date: str
