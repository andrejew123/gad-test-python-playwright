import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestComment:
    def test_add_comment_to_article(self, create_random_article, create_random_comment):
        # Arrange
        article_page, comment_data = create_random_comment

        # Act
        article_comment = article_page.get_article_comment(comment_data.body)

        # Assert
        expect(article_comment.body).to_have_text(comment_data.body)

    def test_open_comment_from_article(self, create_random_article, create_random_comment):
        # Arrange
        article_page, comment_data = create_random_comment
        article_comment = article_page.get_article_comment(comment_data.body)

        # Act
        comment_page = article_page.click_comment_link(article_comment)

        # Assert
        expect(comment_page.comment_body).to_have_text(comment_data.body)
