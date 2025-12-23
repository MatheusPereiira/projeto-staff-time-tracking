from utils.json_manager import JsonManager
from utils.security import hash_password


class UserModel:
    def __init__(self):
        self.storage = JsonManager("data/users.json")


    def all(self):
        return self.storage.read()

    def find_by_username(self, username):
        users = self.storage.read()
        for user in users:
            if user["username"] == username:
                return user
        return None

    def create(self, data):
        users = self.storage.read()
        users.append(data)
        self.storage.write(users)

    def update_password(self, username, new_password):
        users = self.storage.read()
        for user in users:
            if user["username"] == username:
                user["password"] = hash_password(new_password)
                break
        self.storage.write(users)
