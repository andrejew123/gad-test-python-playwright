from faker import Faker

from src.models.comment_model import AddCommentModel

faker = Faker()


def prepare_random_comment(body_sentences: int = 5) -> AddCommentModel:
    body = faker.sentence(nb_words=body_sentences)
    return AddCommentModel(body=body)
