from models.employee_model import EmployeeModel
from models.user_model import UserModel
from utils.security import hash_password


class EmployeeController:
    def __init__(self):
        self.employee_model = EmployeeModel()
        self.user_model = UserModel()

    def all(self):
        return self.employee_model.all()

    def create_with_user(self, data: dict):
        user = self.user_model.add({
            "username": data["username"],
            "password": hash_password(data["password"]),
            "role": "employee"
        })

        employee = self.employee_model.create({
            "name": data["name"],
            "role": data["role"],
            "department": data["department"],
            "user_id": user["id"]
        })

        return employee

    def get_by_username(self, username: str):
        user = self.user_model.find_by_username(username)
        if not user:
            return None
        return self.employee_model.get_by_user_id(user["id"])

    def delete(self, employee_id: str):
        self.employee_model.delete(employee_id)

    def update(self, employee_id: str, data: dict):
        self.employee_model.update(employee_id, data)
