"""Root pytest configuration: browser/page overrides, auth storage state, fixture wiring.

Mirrors the TS project's config/global.setup.ts (auth storage state) and
src/fixtures/*.fixture.ts (page objects, article/comment builders) which are merged
together in src/fixtures/merge.fixture.ts.
"""

import pytest

from config.env_config import BASE_URL
from src.pages.login_page import LoginPage
from src.test_data.user_data import test_user_1

# Re-export fixtures so they're available to every test module.
from src.fixtures.page_object_fixtures import *  # noqa: F401,F403
from src.fixtures.article_fixtures import *  # noqa: F401,F403
from src.fixtures.comment_fixtures import *  # noqa: F401,F403


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "base_url": BASE_URL}


@pytest.fixture(scope="session")
def storage_state_path(browser, browser_context_args, tmp_path_factory):
    """Logs in once per session and persists the storage state to disk.

    Equivalent to the TS `setup` project + `storageState` dependency used by the
    `chromium-logged` project.
    """
    state_path = tmp_path_factory.mktemp("auth") / "session.json"
    context = browser.new_context(**browser_context_args)
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(test_user_1)

    context.storage_state(path=str(state_path))
    context.close()
    return str(state_path)


@pytest.fixture
def page(request, browser, browser_context_args, storage_state_path):
    """Overrides pytest-playwright's `page` fixture to inject an authenticated
    storage state for tests marked with `@pytest.mark.logged`.
    """
    context_args = dict(browser_context_args)
    if request.node.get_closest_marker("logged"):
        context_args["storage_state"] = storage_state_path

    context = browser.new_context(**context_args)
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def api_request_context(playwright):
    """API request context pointed at BASE_URL, mirroring `request` in the TS tests."""
    request_context = playwright.request.new_context(base_url=BASE_URL)
    yield request_context
    request_context.dispose()
