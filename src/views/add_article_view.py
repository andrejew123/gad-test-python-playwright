from playwright.sync_api import Page

from src.models.article_model import AddArticleModel


class AddArticleView:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_new_header = page.get_by_role("heading", name="Add New Entry")
        self.title_input = page.get_by_test_id("title-input")
        self.body_input = page.get_by_test_id("body-text")
        self.save_button = page.get_by_test_id("save")
        self.alert_pop_up = page.get_by_test_id("alert-popup")

    def create_article(self, add_article: AddArticleModel):
        from src.pages.article_page import ArticlePage

        self.title_input.fill(add_article.title)
        self.body_input.fill(add_article.body)
        self.save_button.click()
        return ArticlePage(self.page)
