from models.employee_model import EmployeeModel
from models.user_model import UserModel


class EmployeeController:
    def __init__(self):
        self.employee_model = EmployeeModel()
        self.user_model = UserModel()

    def all(self):
        return self.employee_model.all()

    def create(self, data: dict):
        employee = self.employee_model.create(data)
        return employee

    def update(self, employee_id: str, data: dict):
        self.employee_model.update(employee_id, data)

    def delete(self, employee_id: str):
        self.employee_model.delete(employee_id)

    def get_by_username(self, username: str):
        return self.employee_model.get_by_username(username)
