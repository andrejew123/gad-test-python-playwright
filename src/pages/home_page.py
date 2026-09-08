from playwright.sync_api import Page

from src.pages.base_page import BasePage


class HomePage(BasePage):
    url = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
