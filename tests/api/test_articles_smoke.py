from src.utils.api_util import API_LINKS, get_authorization_header


class TestArticlesSmoke:
    def test_articles_endpoint_is_reachable(self, api_request_context):
        # Arrange
        expected_status_code = 200

        # Act
        response = api_request_context.get(API_LINKS["articles_url"])

        # Assert
        assert response.status == expected_status_code

    def test_login_returns_access_token(self, api_request_context):
        # Act
        headers = get_authorization_header(api_request_context)

        # Assert
        assert headers["Authorization"].startswith("Bearer ")
