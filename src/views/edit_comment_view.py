from playwright.sync_api import Page

from src.models.comment_model import AddCommentModel


class EditCommentView:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.body_input = page.locator("#body")
        self.update_button = page.get_by_test_id("update-button")

    def update_comment(self, comment_data: AddCommentModel):
        from src.pages.comment_page import CommentPage

        self.body_input.fill(comment_data.body)
        self.update_button.click()
        return CommentPage(self.page)
