from playwright.sync_api import expect

from src.factories.user_factory import prepare_random_user


class TestRegister:
    def test_register_with_valid_data(self, register_page):
        # Arrange
        expected_login_title = "Login"
        register_user_data = prepare_random_user()

        # Act
        login_page = register_page.register(register_user_data)
        title = login_page.get_title()

        # Assert
        assert expected_login_title in title

    def test_reject_register_with_invalid_email(self, register_page):
        # Arrange
        register_user_data = prepare_random_user()
        register_user_data.user_email = "not-an-email"

        # Act
        register_page.register(register_user_data)

        # Assert
        expect(register_page.expected_error_text).to_be_visible()
