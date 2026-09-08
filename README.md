# GAD Tests (Python + Playwright)

Python/pytest port of the TypeScript Playwright framework in the repo root, following the
same Page Object Model, fixtures, factories and test-layout conventions.

## Setup

```bash
cd python-playwright-tests
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install
copy .env.example .env         # then fill in BASE_URL / USER_EMAIL / USER_PASSWORD
```

## Running tests

```bash
pytest                              # all tests, headless
pytest --headed                     # headed browser
pytest tests/ui                     # UI tests only
pytest tests/api                    # API tests only
pytest -m logged                    # only tests requiring an authenticated session
pytest -m "not logged"              # only tests that don't require login
pytest -k "login"                   # tests matching a keyword
```

HTML/trace artifacts are written to `test-results/` (traces, screenshots, videos on failure).
Open a trace with `playwright show-trace test-results/.../trace.zip`.

## Structure

```
config/            environment configuration (env_config.py)
src/
  pages/           page objects (mirrors src/pages in the TS project)
  components/      shared page fragments (e.g. main menu)
  views/           in-page views/dialogs (add article, add/edit comment)
  models/          dataclasses describing form/API payloads
  factories/        Faker-based random data builders
  test_data/       static test data (credentials, etc.)
  utils/           api & wait helpers
  fixtures/        pytest fixtures (page objects, article/comment builders)
tests/
  ui/
    smoke/         fast sanity checks
    integration/   single-page/flow tests
    end_to_end/    multi-step user journeys
  api/             REST API tests
conftest.py        wires up fixtures, browser/context/page overrides
```

## Authenticated tests

Mark a test with `@pytest.mark.logged` to have the `page` fixture use a storage state that
was captured by logging in once per session (equivalent to the TS `setup` project +
`storageState` dependency):

```python
import pytest

@pytest.mark.logged
def test_something(articles_page):
    ...
```

## Conventions

- snake_case for functions/variables, PascalCase for classes, matching `CODING_STANDARS.md`
  in the repo root (AAA test structure, page objects return page objects, avoid assertion
  messages unless useful, extract expected values into variables before asserting).
- Page object methods that navigate return the new page object instead of `None`.
