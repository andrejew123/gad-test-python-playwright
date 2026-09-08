from playwright.sync_api import Page, Response

RESPONSE_TIMEOUT = 10_000


def wait_for_response(
    page: Page,
    url: str,
    method: str | None = None,
    status: int | None = None,
    text: str | None = None,
) -> Response:
    def predicate(response: Response) -> bool:
        if url not in response.url:
            return False
        if method and response.request.method != method:
            return False
        if status and response.status != status:
            return False
        if text and text not in response.text():
            return False
        return True

    return page.wait_for_response(predicate, timeout=RESPONSE_TIMEOUT)
