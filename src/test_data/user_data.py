from config.env_config import USER_EMAIL, USER_PASSWORD
from src.models.user_model import LoginUserModel

test_user_1 = LoginUserModel(user_email=USER_EMAIL, user_password=USER_PASSWORD)
