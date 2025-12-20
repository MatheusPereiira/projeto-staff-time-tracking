from utils.json_manager import JsonManager


class UserModel:
    def __init__(self):
        self.storage = JsonManager("data/users.json")

    def all(self):
        return self.storage.read()

    def find_by_username(self, username):
        users = self.storage.read()
        return next((u for u in users if u["username"] == username), None)

    def create(self, data):
        users = self.storage.read()
        users.append(data)
        self.storage.write(users)
