from playwright.sync_api import Page

from src.components.main_menu_component import MainMenuComponent
from src.pages.base_page import BasePage


class HomePage(BasePage):
    url = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.main_menu = MainMenuComponent(page)
