import pytest

from conftest import api_request_context
from src.utils.api_util import (
    API_LINKS,
    get_authorization_header,
    prepare_article_payload,
    prepare_comment_payload,
)


class TestCommentsIntegration:
    @pytest.fixture(autouse=True)
    def _setup(self, api_request_context):
        self.headers = get_authorization_header(api_request_context)
        article_data = prepare_article_payload()
        response_article = api_request_context.post(
            API_LINKS["articles_url"], headers=self.headers, data=article_data
        )
        article_json = response_article.json()
        self.article_id = article_json["id"]

    def test_should_create_comment_with_logged_in_user(self, api_request_context):
        # Arrange
        expected_status_code = 201
        comment_data = prepare_comment_payload(self.article_id)

        # Act
        self.response_comment = api_request_context.post(
            API_LINKS["comments_url"], headers=self.headers, data=comment_data
        )

        # Assert
        assert self.response_comment.status == expected_status_code
        comment_json = self.response_comment.json()
        assert comment_json["body"] == comment_data["body"]
        assert comment_json["article_id"] == self.article_id

    def test_should_not_create_comment_without_logged_in_user(self, api_request_context):
        # Arrange
        expected_status_code = 401
        comment_data = prepare_comment_payload(self.article_id)

        # Act
        response = api_request_context.post(API_LINKS["comments_url"], data=comment_data)

        # Assert
        assert response.status == expected_status_code

    def test_should_delete_comment_with_logged_in_user(self, api_request_context):
        # Arrange
        expected_status_code = 200
        comment_data = prepare_comment_payload(self.article_id)

        # Act
        response_comment = api_request_context.post(API_LINKS["comments_url"], headers=self.headers, data=comment_data)
        comment_json = response_comment.json()
        comment_id = comment_json["id"]
        response_delete = api_request_context.delete(f"{API_LINKS['comments_url']}/{comment_id}", headers=self.headers,)

        # Assert
        assert response_delete.status == expected_status_code