from src.api.utils.api_util import API_LINKS


class TestCommentsSmoke:
    def test_comments_endpoint_is_reachable(self, api_request_context):
        # Arrange
        expected_status_code = 200

        # Act
        response = api_request_context.get(API_LINKS["comments_url"])

        # Assert
        assert response.status == expected_status_code
