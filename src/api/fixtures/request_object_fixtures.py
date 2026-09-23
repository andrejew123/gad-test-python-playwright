"""Request-object fixtures"""

import pytest

from api.requests.articles_requests import ArticlesRequests


@pytest.fixture
def article_request(api_request_context) -> ArticlesRequests:
    return ArticlesRequests(api_request_context)
