import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestArticle:
    def test_non_logged_user_can_access_created_article(self, create_random_article, articles_page):
        # Arrange
        articles_page.goto('?id=1')
        article_page, article_data = create_random_article
        # Assert
        expect(article_page.article_title).to_have_text(article_data.title)
        expect(article_page.article_body).to_contain_text(article_data.body[:20])
