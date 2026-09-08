from playwright.sync_api import expect


class TestSearch:
    def test_search_with_no_results_shows_message(self, articles_page):
        # Arrange
        search_phrase = "zzz-does-not-exist-zzz"

        # Act
        articles_page.search_article(search_phrase)

        # Assert
        expect(articles_page.no_result_text).to_be_visible()

    def test_clearing_search_shows_all_articles_again(self, articles_page):
        # Arrange
        search_phrase = "zzz-does-not-exist-zzz"
        articles_page.search_article(search_phrase)

        # Act
        articles_page.search_article("")

        # Assert
        expect(articles_page.no_result_text).not_to_be_visible()
