from playwright.sync_api import APIRequestContext

from src.test_data.user_data import test_user_1


def get_authorization_header(request: APIRequestContext) -> dict[str, str]:
    login_url = "/api/login"
    response = request.post(
        login_url,
        data={
            "email": test_user_1.user_email,
            "password": test_user_1.user_password,
        },
    )
    response_json = response.json()
    return {"Authorization": f"Bearer {response_json['access_token']}"}
