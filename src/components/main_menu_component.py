from playwright.sync_api import Page


class MainMenuComponent:
    """Navigation bar present across authenticated pages."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.comments_button = page.get_by_test_id("open-comments")
        self.articles_button = page.get_by_test_id("open-articles")
        self.home_page_link = page.get_by_role("link", name="🦎 GAD")

    def click_comments_button(self):
        from src.pages.comments_page import CommentsPage

        self.comments_button.click()
        return CommentsPage(self.page)

    def click_articles_button(self):
        from src.pages.articles_page import ArticlesPage

        self.articles_button.click()
        return ArticlesPage(self.page)

    def click_home_page_button(self):
        from src.pages.home_page import HomePage

        self.home_page_link.click()
        return HomePage(self.page)
