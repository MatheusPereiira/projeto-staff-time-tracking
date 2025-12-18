from models.employee_model import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()

    def list_all(self):
        return self.model.all()

    def create(self, name, username, role, department):
        employee = {
            "name": name,
            "username": username,
            "role": role,
            "department": department
        }
        self.model.add(employee)

    def get_by_username(self, username):
        return self.model.find_by_username(username)
