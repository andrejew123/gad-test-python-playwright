import os

from dotenv import load_dotenv

load_dotenv(override=True)


def require_env_variable(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Environment variable {name} is not set.")
    return value


BASE_URL = require_env_variable("BASE_URL")
USER_EMAIL = require_env_variable("USER_EMAIL")
USER_PASSWORD = require_env_variable("USER_PASSWORD")
