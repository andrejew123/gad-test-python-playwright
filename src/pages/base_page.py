from playwright.sync_api import Page


class BasePage:
    """Common navigation helpers shared by all page objects."""

    url: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, parameters: str = "") -> None:
        self.page.goto(f"{self.url}{parameters}")

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_page_to_load_url(self) -> None:
        self.page.wait_for_url(self.url)
