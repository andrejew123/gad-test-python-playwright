class TestWebpage:
    def test_home_page_loads(self, home_page):
        # Arrange
        expected_title_fragment = ""

        # Act
        title = home_page.get_title()

        # Assert
        assert isinstance(title, str)
        assert expected_title_fragment in title

    def test_login_page_loads(self, login_page):
        # Assert
        assert login_page.login_button.is_visible()

    def test_register_page_loads(self, register_page):
        # Assert
        assert register_page.register_button.is_visible()
