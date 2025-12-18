from utils.json_manager import JSONManager


class UserModel:
    def __init__(self):
        self.db = JSONManager("users.json")

    def all(self) -> list:
        return self.db.read()

    def add(self, user: dict):
        users = self.all()
        users.append(user)
        self.db.write(users)

    def find_by_username(self, username: str):
        for user in self.all():
            if user["username"] == username:
                return user
        return None
