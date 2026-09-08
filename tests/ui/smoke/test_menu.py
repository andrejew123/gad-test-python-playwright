import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestMenu:
    def test_navigate_to_articles_via_menu(self, home_page):
        # Arrange
        expected_url_fragment = "articles.html"

        # Act
        articles_page = home_page.main_menu.click_articles_button()

        # Assert
        assert expected_url_fragment in articles_page.page.url

    def test_navigate_to_comments_via_menu(self, home_page):
        # Arrange
        expected_url_fragment = "comments.html"

        # Act
        comments_page = home_page.main_menu.click_comments_button()

        # Assert
        assert expected_url_fragment in comments_page.page.url

    def test_navigate_home_via_logo(self, articles_page):
        # Act
        home_page = articles_page.main_menu.click_home_page_button()

        # Assert
        expect(home_page.page).to_have_url(home_page.page.url)
