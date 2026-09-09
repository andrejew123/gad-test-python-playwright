"""Root pytest configuration: browser/page overrides, auth storage state, fixture wiring.

Mirrors the TS project's config/global.setup.ts (auth storage state) and
src/fixtures/*.fixture.ts (page objects, article/comment builders) which are merged
together in src/fixtures/merge.fixture.ts.
"""

from urllib.parse import urlsplit, urlunsplit

import pytest

from config.env_config import BASE_URL

# Re-export fixtures so they're available to every test module.
from src.fixtures.article_fixtures import *  # noqa: F401,F403
from src.fixtures.comment_fixtures import *  # noqa: F401,F403
from src.fixtures.page_object_fixtures import *  # noqa: F401,F403
from src.pages.login_page import LoginPage
from src.test_data.user_data import test_user_1


def _api_base_url(base_url: str) -> str:
    """Force IPv4 loopback for localhost to avoid ::1 ECONNREFUSED on some setups."""
    parsed = urlsplit(base_url)
    if parsed.hostname != "localhost":
        return base_url

    port = f":{parsed.port}" if parsed.port is not None else ""
    ipv4_netloc = f"127.0.0.1{port}"
    return urlunsplit((parsed.scheme, ipv4_netloc, parsed.path, parsed.query, parsed.fragment))


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
def context(request, new_context, storage_state_path):
    """Override pytest-playwright's context fixture while still using its
    context factory so tracing/screenshot/video artifacts are persisted.
    """
    if request.node.get_closest_marker("logged"):
        return new_context(storage_state=storage_state_path)
    return new_context()


@pytest.fixture
def api_request_context(playwright):
    """API request context pointed at BASE_URL, mirroring `request` in the TS tests."""
    request_context = playwright.request.new_context(base_url=_api_base_url(BASE_URL))
    yield request_context
    request_context.dispose()
