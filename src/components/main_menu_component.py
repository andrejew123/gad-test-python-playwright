from playwright.sync_api import Page


class MainMenuComponent:
    """Navigation bar present across authenticated pages."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.comments_button = page.locator(
            '[data-testid="open-comments"], a[href*="comments.html"], a[href*="/comments"]'
        ).first
        self.articles_button = page.locator(
            '[data-testid="open-articles"], a[href*="articles.html"], a[href*="/articles"]'
        ).first
        self.home_page_link = page.get_by_role("link", name="🦎 GAD")

    def click_comments_button(self):
        from src.pages.comments_page import CommentsPage

        # On the home dashboard, comments navigation is reached through Articles first.
        if self.comments_button.count() == 0:
            if self.articles_button.count() == 0:
                raise RuntimeError("Comments navigation item is not available on this page.")
            self.articles_button.click()

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
