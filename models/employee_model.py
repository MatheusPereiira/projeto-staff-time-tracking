from utils.json_manager import JSONManager


class EmployeeModel:
    def __init__(self):
        self.db = JSONManager("employees.json")

    def all(self):
        return self.db.read()

    def add(self, employee: dict):
        data = self.db.read()
        data.append( employee )
        self.db.write(data)

    def find_by_username(self, username: str):
        for emp in self.db.read():
            if emp.get("username") == username:
                return emp
        return None
