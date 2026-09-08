"""Page-object fixtures, mirroring src/fixtures/page-object.fixture.ts."""

import pytest

from src.pages.article_page import ArticlePage
from src.pages.articles_page import ArticlesPage
from src.pages.comment_page import CommentPage
from src.pages.comments_page import CommentsPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage
from src.views.add_article_view import AddArticleView


@pytest.fixture
def home_page(page) -> HomePage:
    home = HomePage(page)
    home.goto()
    return home


@pytest.fixture
def login_page(page) -> LoginPage:
    login = LoginPage(page)
    login.goto()
    return login


@pytest.fixture
def register_page(page) -> RegisterPage:
    register = RegisterPage(page)
    register.goto()
    return register


@pytest.fixture
def articles_page(page) -> ArticlesPage:
    articles = ArticlesPage(page)
    articles.goto()
    return articles


@pytest.fixture
def article_page(page) -> ArticlePage:
    return ArticlePage(page)


@pytest.fixture
def comments_page(page) -> CommentsPage:
    comments = CommentsPage(page)
    comments.goto()
    return comments


@pytest.fixture
def comment_page(page) -> CommentPage:
    return CommentPage(page)


@pytest.fixture
def add_article_view(articles_page) -> AddArticleView:
    return articles_page.click_add_article_button_logged()
