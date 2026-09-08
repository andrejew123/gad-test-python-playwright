from playwright.sync_api import Page

from src.components.main_menu_component import MainMenuComponent
from src.pages.base_page import BasePage


class CommentPage(BasePage):
    url = "/comment.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.main_menu = MainMenuComponent(page)
        self.comment_body = page.get_by_test_id("comment-body")
        self.edit_button = page.get_by_test_id("edit")
        self.alert_pop_up = page.get_by_test_id("alert-popup")
        self.return_link = page.get_by_test_id("return")

    def click_edit_button(self):
        from src.views.edit_comment_view import EditCommentView

        self.edit_button.click()
        return EditCommentView(self.page)

    def click_return_link(self):
        from src.pages.article_page import ArticlePage

        self.return_link.click()
        return ArticlePage(self.page)
