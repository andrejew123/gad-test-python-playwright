import pytest
from playwright.sync_api import expect


@pytest.mark.logged
class TestArticleLifecycle:
    def test_create_comment_on_and_delete_article(self, create_random_article, random_comment):
        # Arrange
        article_page, article_data = create_random_article
        comment_data = random_comment()

        # Act - add a comment to the freshly created article
        add_comment_view = article_page.click_add_comment_button()
        article_page = add_comment_view.create_comment(comment_data)
        article_comment = article_page.get_article_comment(comment_data.body)

        # Assert - comment is visible on the article
        expect(article_comment.body).to_have_text(comment_data.body)
        expect(article_page.article_title).to_have_text(article_data.title)

        # Act - delete the article
        articles_page = article_page.delete_article()

        # Assert - article no longer listed
        expect(articles_page.page.get_by_text(article_data.title)).not_to_be_visible()
