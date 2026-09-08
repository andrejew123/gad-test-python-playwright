from playwright.sync_api import Page

from src.models.user_model import RegisterUserModel
from src.pages.base_page import BasePage


class RegisterPage(BasePage):
    url = "/register.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_first_name_input = page.get_by_test_id("firstname-input")
        self.user_last_name_input = page.get_by_test_id("lastname-input")
        self.user_email_input = page.get_by_test_id("email-input")
        self.user_password_input = page.get_by_test_id("password-input")
        self.register_button = page.get_by_test_id("register-button")
        self.alert_pop_up = page.get_by_test_id("alert-popup")
        self.expected_error_text = page.locator("#octavalidate_email")

    def register(self, register_user_data: RegisterUserModel):
        from src.pages.login_page import LoginPage

        self.user_first_name_input.fill(register_user_data.user_first_name)
        self.user_last_name_input.fill(register_user_data.user_last_name)
        self.user_email_input.fill(register_user_data.user_email)
        self.user_password_input.fill(register_user_data.user_password)
        self.register_button.click()
        return LoginPage(self.page)
