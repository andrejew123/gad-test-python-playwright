from dataclasses import dataclass


@dataclass
class RegisterUserModel:
    user_first_name: str
    user_last_name: str
    user_email: str
    user_password: str


@dataclass
class LoginUserModel:
    user_email: str
    user_password: str
