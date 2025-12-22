from models.employee_model import EmployeeModel
from models.user_model import UserModel


class EmployeeController:
    def __init__(self):
        self.employee_model = EmployeeModel()
        self.user_model = UserModel()

    def all(self):
        return self.employee_model.all()

    def get_by_username(self, username: str):
        return self.employee_model.get_by_username(username)

    def create_with_user(self, data: dict):
        # cria usuário
        self.user_model.create({
            "username": data["username"],
            "password": data["password"],
            "role": "employee"
        })

        # cria funcionário vinculado ao usuário
        return self.employee_model.create(data)

    def delete(self, employee_id: str):
        return self.employee_model.delete(employee_id)

    def update(self, employee_id: str, data: dict):
        return self.employee_model.update(employee_id, data)
