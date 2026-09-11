"""Comment-creation fixtures, mirroring the article fixture pattern for comments."""

import pytest

from src.factories.comment_payload_factory import prepare_random_comment
from src.models.comment_model import AddCommentModel


@pytest.fixture
def create_random_comment(article_page):
    """Adds a random comment to the current article and returns (article_page, comment_data)."""
    comment_data = prepare_random_comment()
    add_comment_view = article_page.click_add_comment_button()
    article_page = add_comment_view.create_comment(comment_data)
    return article_page, comment_data


@pytest.fixture
def random_comment():
    """Factory fixture: call with optional AddCommentModel to build random comment data."""

    def _create(comment_data: AddCommentModel | None = None) -> AddCommentModel:
        return comment_data or prepare_random_comment()

    return _create
