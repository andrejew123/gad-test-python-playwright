from playwright.sync_api import Page

from src.models.user_model import LoginUserModel
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    url = "/login/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_email_input = page.get_by_role("textbox", name="Enter User Email")
        self.user_password_input = page.get_by_role("textbox", name="Enter Password")
        self.login_button = page.get_by_role("button", name="LogIn")
        self.login_error = page.get_by_test_id("login-error")

    def login(self, login_user_data: LoginUserModel):
        from src.pages.welcome_page import WelcomePage

        self.user_email_input.fill(login_user_data.user_email)
        self.user_password_input.fill(login_user_data.user_password)
        self.login_button.click()
        return WelcomePage(self.page)
