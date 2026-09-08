from playwright.sync_api import Page

from src.components.main_menu_component import MainMenuComponent
from src.pages.base_page import BasePage


class ArticlesPage(BasePage):
    url = "/articles.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.main_menu = MainMenuComponent(page)
        self.add_article_button_logged = page.locator("#add-new")
        self.search_input = page.get_by_test_id("search-input")
        self.go_search_button = page.get_by_test_id("search-button")
        self.no_result_text = page.get_by_test_id("no-results")

    def go_to_article(self, title: str):
        from src.pages.article_page import ArticlePage

        self.page.get_by_text(title).click()
        return ArticlePage(self.page)

    def search_article(self, phrase: str) -> "ArticlesPage":
        self.search_input.fill(phrase)
        self.go_search_button.click()
        return self

    def click_add_article_button_logged(self):
        from src.views.add_article_view import AddArticleView

        self.add_article_button_logged.click()
        return AddArticleView(self.page)
