import re

from faker import Faker

from src.models.user_model import RegisterUserModel

faker = Faker()


def prepare_random_user() -> RegisterUserModel:
    first_name = re.sub(r"[^A-Za-z]", "", faker.first_name())
    last_name = re.sub(r"[^A-Za-z]", "", faker.last_name())
    email = faker.email()
    password = faker.password()

    return RegisterUserModel(
        user_first_name=first_name,
        user_last_name=last_name,
        user_email=email,
        user_password=password,
    )
