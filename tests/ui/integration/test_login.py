import pytest
from faker import Faker

from src.models.user_model import LoginUserModel
from src.test_data.user_data import test_user_1

faker = Faker()


class TestLogin:
    def test_login_with_correct_credentials(self, login_page):
        # Arrange
        expected_welcome_title = "Welcome"

        # Act
        welcome_page = login_page.login(test_user_1)
        title = welcome_page.get_title()

        # Assert
        assert expected_welcome_title in title

    def test_reject_login_with_incorrect_password(self, login_page):
        # Arrange
        login_user_data = LoginUserModel(
            user_email=test_user_1.user_email, user_password=faker.password()
        )
        expected_login_title = "Login"
        expected_error_text = "Invalid username or password"

        # Act
        login_page.login(login_user_data)
        title = login_page.get_title()

        # Assert
        assert login_page.login_error.inner_text() == expected_error_text
        assert expected_login_title in title
