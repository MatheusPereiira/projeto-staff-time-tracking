from models.employee_model import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()

    def all(self):
        return self.model.all()

    def add(self, employee: dict):
        self.model.add(employee)

    def get_by_username(self, username: str):
        return self.model.find_by_username(username)
