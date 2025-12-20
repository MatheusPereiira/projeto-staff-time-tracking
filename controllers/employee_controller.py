from models.employee_model import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()

    def all(self):
        return self.model.all()

    def create(self, data: dict):
        return self.model.create(data)

    def delete(self, employee_id: str):
        return self.model.delete(employee_id)

    def update(self, employee_id: str, data: dict):
        return self.model.update(employee_id, data)
