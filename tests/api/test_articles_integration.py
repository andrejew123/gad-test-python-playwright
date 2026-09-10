import time

import pytest

from src.api.utils.api_util import API_LINKS
from src.api.factories.article_payload_api_factory import prepare_article_payload
from src.api.factories.authorization_header_api_factory import get_authorization_header


def wait_until(action, condition, timeout=2.0, interval=0.1):
    deadline = time.monotonic() + timeout
    while True:
        result = action()

        if condition(result):
            return result

        if time.monotonic() >= deadline:
            raise AssertionError(f"Condition not met within {timeout}s")
        time.sleep(interval)


class TestArticlesIntegration:
    def test_should_not_create_article_without_logged_in_user(self, api_request_context):
        # Arrange
        expected_status_code = 401
        article_data = prepare_article_payload()

        # Act
        response = api_request_context.post(API_LINKS["articles_url"], data=article_data)

        # Assert
        assert response.status == expected_status_code

    class TestCrudOperations:
        @pytest.fixture(autouse=True)
        def _setup(self, api_request_context):
            self.headers = get_authorization_header(api_request_context)
            self.article_data = prepare_article_payload()
            self.response_article = api_request_context.post(
                API_LINKS["articles_url"], headers=self.headers, data=self.article_data
            )
            article_json = self.response_article.json()
            article_id = article_json["id"]
            wait_until(
                action=lambda: api_request_context.get(f"{API_LINKS['articles_url']}/{article_id}"),
                condition=lambda response: response.status == 200,
                timeout=2,
            )

        def test_should_create_article_with_logged_in_user(self):
            # Arrange
            expected_status_code = 201

            # Assert
            actual_status = self.response_article.status
            assert actual_status == expected_status_code

            article_json = self.response_article.json()
            assert article_json["title"] == self.article_data["title"]
            assert article_json["body"] == self.article_data["body"]

        def test_should_delete_article_with_logged_in_user(self, api_request_context):
            # Arrange
            expected_status_code = 200
            expected_deleted_status_code = 404
            article_json = self.response_article.json()
            article_id = article_json["id"]

            # Act
            response_delete = api_request_context.delete(
                f"{API_LINKS['articles_url']}/{article_id}", headers=self.headers
            )

            # Assert
            assert response_delete.status == expected_status_code

            response_get = api_request_context.get(
                f"{API_LINKS['articles_url']}/{article_id}", headers=self.headers
            )
            assert response_get.status == expected_deleted_status_code

        def test_should_not_delete_article_with_non_logged_in_user(self, api_request_context):
            # Arrange
            expected_status_code = 401
            article_json = self.response_article.json()
            article_id = article_json["id"]

            # Act
            response_delete = api_request_context.delete(
                f"{API_LINKS['articles_url']}/{article_id}"
            )

            # Assert
            assert response_delete.status == expected_status_code
