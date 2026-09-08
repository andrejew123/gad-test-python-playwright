from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from src.components.main_menu_component import MainMenuComponent
from src.pages.base_page import BasePage


@dataclass
class ArticleComment:
    body: Locator
    link: Locator


class ArticlePage(BasePage):
    url = "/article.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.main_menu = MainMenuComponent(page)
        self.article_title = page.get_by_test_id("article-title")
        self.article_body = page.get_by_test_id("article-body")
        self.delete_icon = page.get_by_test_id("delete")
        self.add_comment_button = page.locator("#add-new")
        self.alert_pop_up = page.get_by_test_id("alert-popup")

    def click_add_comment_button(self):
        from src.views.add_comment_view import AddCommentView

        self.add_comment_button.click()
        return AddCommentView(self.page)

    def delete_article(self):
        from src.pages.articles_page import ArticlesPage

        self.page.on("dialog", lambda dialog: dialog.accept())
        self.delete_icon.click()
        return ArticlesPage(self.page)

    def get_article_comment(self, body: str) -> ArticleComment:
        comment_container = self.page.locator(".comment-container").filter(has_text=body)
        return ArticleComment(
            body=comment_container.locator(':text("comment:") + span'),
            link=comment_container.locator("[id^='gotoComment']"),
        )

    def click_comment_link(self, article_comment: ArticleComment):
        from src.pages.comment_page import CommentPage

        article_comment.link.click()
        return CommentPage(self.page)
