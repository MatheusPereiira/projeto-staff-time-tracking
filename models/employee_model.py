import uuid
from utils.json_manager import JsonManager


class EmployeeModel:
    def __init__(self):
        self.storage = JsonManager("data/employees.json")

    def all(self):
        return self.storage.read()

    def create(self, data: dict):
        employees = self.storage.read()

        new_employee = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "role": data["role"],
            "department": data["department"]
        }

        employees.append(new_employee)
        self.storage.write(employees)
        return new_employee

    def delete(self, employee_id: str):
        employees = self.storage.read()
        new_list = [e for e in employees if e["id"] != employee_id]
        self.storage.write(new_list)
        return True

    def update(self, employee_id: str, data: dict):
        employees = self.storage.read()

        for emp in employees:
            if emp["id"] == employee_id:
                emp["name"] = data["name"]
                emp["role"] = data["role"]
                emp["department"] = data["department"]
                break

        self.storage.write(employees)
        return True
