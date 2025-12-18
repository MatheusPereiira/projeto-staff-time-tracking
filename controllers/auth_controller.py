from models.user_model import UserModel
from utils.security import verify_password


class AuthController:
    def __init__(self):
        self.model = UserModel()

    def login(self, username: str, password: str):
        user = self.model.find_by_username(username)

        if not user:
            return None

        if verify_password(password, user["password"]):
            return user

        return None
