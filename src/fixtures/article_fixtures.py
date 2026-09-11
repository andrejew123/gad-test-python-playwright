"""Article-creation fixtures, mirroring src/fixtures/article.fixture.ts."""

import pytest

from src.factories.articles_payload_factory import prepare_random_article
from src.models.article_model import AddArticleModel


@pytest.fixture
def create_random_article(add_article_view):
    """Creates a random article and returns (article_page, article_data)."""
    article_data = prepare_random_article()
    article_page = add_article_view.create_article(article_data)
    return article_page, article_data


@pytest.fixture
def random_article(add_article_view):
    """Factory fixture: call with optional AddArticleModel to create an article on demand."""

    def _create(article_data: AddArticleModel | None = None):
        final_article_data = article_data or prepare_random_article()
        article_page = add_article_view.create_article(final_article_data)
        return article_page, final_article_data

    return _create
