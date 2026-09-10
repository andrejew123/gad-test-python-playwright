from pydantic import BaseModel


class AddCommentModel(BaseModel):
    body: str
