from pydantic import BaseModel


class AddArticleModel(BaseModel):
    title: str
    body: str
