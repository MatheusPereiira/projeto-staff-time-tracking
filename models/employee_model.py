import uuid
from utils.json_manager import JsonManager


class EmployeeModel:
    def __init__(self):
        self.storage = JsonManager("data/employees.json")

    def all(self):
        return self.storage.read()

    def get_by_user_id(self, user_id: str):
        for emp in self.all():
            if emp.get("user_id") == user_id:
                return emp
        return None

    def create(self, data: dict):
        employees = self.all()

        new_employee = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "role": data["role"],
            "department": data["department"],
            "user_id": data["user_id"]
        }

        employees.append(new_employee)
        self.storage.write(employees)
        return new_employee

    def delete(self, employee_id: str):
        employees = [e for e in self.all() if e["id"] != employee_id]
        self.storage.write(employees)

    def update(self, employee_id: str, data: dict):
        employees = self.all()
        for emp in employees:
            if emp["id"] == employee_id:
                emp.update(data)
                break
        self.storage.write(employees)
