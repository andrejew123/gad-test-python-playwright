from src.api.models.article_api_models import ArticlePayload
from src.api.utils.api_util import _current_utc_timestamp
from src.factories.articles_factory import prepare_random_article


def prepare_article_payload() -> ArticlePayload:
    random_article = prepare_random_article()
    return {
        "title": random_article.title,
        "body": random_article.body,
        "date": _current_utc_timestamp(),
        "image": "",
    }

