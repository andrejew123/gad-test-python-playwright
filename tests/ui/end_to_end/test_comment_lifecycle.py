import pytest
from playwright.sync_api import expect

from src.factories.comment_payload_factory import prepare_random_comment


@pytest.mark.logged
class TestCommentLifecycle:
    def test_create_edit_and_reopen_comment(self, create_random_article):
        # Arrange
        article_page, _ = create_random_article
        original_comment = prepare_random_comment()
        updated_comment = prepare_random_comment()

        # Act - create the comment
        add_comment_view = article_page.click_add_comment_button()
        article_page = add_comment_view.create_comment(original_comment)
        article_comment = article_page.get_article_comment(original_comment.body)
        comment_page = article_page.click_comment_link(article_comment)

        # Assert - comment created with expected body
        expect(comment_page.comment_body).to_have_text(original_comment.body)

        # Act - edit the comment
        edit_comment_view = comment_page.click_edit_button()
        comment_page = edit_comment_view.update_comment(updated_comment)

        # Assert - comment updated
        expect(comment_page.comment_body).to_have_text(updated_comment.body)

        # Act - return to the article
        article_page = comment_page.click_return_link()

        # Assert - updated comment visible on the article
        updated_article_comment = article_page.get_article_comment(updated_comment.body)
        expect(updated_article_comment.body).to_have_text(updated_comment.body)
