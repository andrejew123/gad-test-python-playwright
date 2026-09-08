import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestArticle:
    def test_create_article_shows_title_and_body(self, create_random_article):
        # Arrange
        article_page, article_data = create_random_article

        # Act
        # (creation already performed by the create_random_article fixture)

        # Assert
        expect(article_page.article_title).to_have_text(article_data.title)
        expect(article_page.article_body).to_contain_text(article_data.body[:20])

    def test_delete_article_navigates_back_to_articles(self, create_random_article):
        # Arrange
        article_page, _ = create_random_article
        expected_url_fragment = "articles.html"

        # Act
        articles_page = article_page.delete_article()

        # Assert
        assert expected_url_fragment in articles_page.page.url
