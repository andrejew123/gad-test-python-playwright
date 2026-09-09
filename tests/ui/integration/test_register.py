import re

from playwright.sync_api import expect

from src.factories.user_factory import prepare_random_user


class TestRegister:
    def test_register_with_valid_data(self, register_page):
        # Arrange
        expected_login_title = re.compile(r".*Login.*")
        register_user_data = prepare_random_user()

        # Act
        login_page = register_page.register(register_user_data)
        login_page.wait_for_page_to_load_url()

        # Assert
        expect(login_page.page).to_have_title(expected_login_title)

    def test_reject_register_with_invalid_email(self, register_page):
        # Arrange
        register_user_data = prepare_random_user()
        register_user_data.user_email = "not-an-email"

        # Act
        register_page.register(register_user_data)

        # Assert
        expect(register_page.expected_error_text).to_be_visible()
