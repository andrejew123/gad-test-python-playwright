import string

from faker import Faker

from src.models.article_model import AddArticleModel

faker = Faker()


def prepare_random_article(
    title_length: int | None = None, body_paragraphs: int = 5
) -> AddArticleModel:
    if title_length:
        title = faker.lexify("?" * title_length, letters=string.ascii_letters)
    else:
        title = faker.sentence()

    body = "\n".join(faker.paragraphs(nb=body_paragraphs))

    return AddArticleModel(title=title, body=body)
