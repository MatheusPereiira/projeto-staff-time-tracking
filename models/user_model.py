import uuid
from utils.json_manager import JsonManager


class UserModel:
    def __init__(self):
        self.storage = JsonManager("data/users.json")

    def all(self):
        return self.storage.read()

    def find_by_username(self, username: str):
        for user in self.all():
            if user["username"] == username:
                return user
        return None

    def add(self, data: dict):
        users = self.all()

        if self.find_by_username(data["username"]):
            raise ValueError("Usuário já existe.")

        new_user = {
            "id": str(uuid.uuid4()),
            "username": data["username"],
            "password": data["password"],
            "role": data.get("role", "employee")
        }

        users.append(new_user)
        self.storage.write(users)
        return new_user
