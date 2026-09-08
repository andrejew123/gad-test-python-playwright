from dataclasses import dataclass


@dataclass
class AddArticleModel:
    title: str
    body: str
