from playwright.sync_api import Page

from src.models.comment_model import AddCommentModel


class AddCommentView:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.body_input = page.locator("#body")
        self.save_button = page.get_by_role("button", name="Save")
        self.add_new_header = page.get_by_role("heading", name="Add New Comment")

    def create_comment(self, comment_data: AddCommentModel):
        from src.pages.article_page import ArticlePage

        self.body_input.fill(comment_data.body)
        self.save_button.click()
        return ArticlePage(self.page)
