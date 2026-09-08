import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestArticles:
    def test_search_article_returns_matching_result(self, create_random_article, articles_page):
        # Arrange
        _, article_data = create_random_article
        articles_page.goto()

        # Act
        articles_page.search_article(article_data.title)

        # Assert
        expect(articles_page.page.get_by_text(article_data.title)).to_be_visible()

    def test_search_article_with_no_match_shows_no_results(self, articles_page):
        # Arrange
        expected_no_result_phrase = "zzz-does-not-exist-zzz"

        # Act
        articles_page.search_article(expected_no_result_phrase)

        # Assert
        expect(articles_page.no_result_text).to_be_visible()
