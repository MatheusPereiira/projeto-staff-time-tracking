from utils.json_manager import JSONManager


class EmployeeModel:
    def __init__(self):
        self.manager = JSONManager("employees.json")

    def all(self):
        return self.manager.read()

    def add(self, name: str, role: str, department: str):
        employees = self.manager.read()

        employee = {
            "id": len(employees) + 1,
            "name": name,
            "role": role,
            "department": department
        }

        employees.append(employee)
        self.manager.write(employees)

        return employee

    def delete(self, employee_id: int):
        employees = self.manager.read()
        employees = [e for e in employees if e["id"] != employee_id]
        self.manager.write(employees)

    def update(self, employee_id: int, name: str, role: str, department: str):
        employees = self.manager.read()

        for e in employees:
            if e["id"] == employee_id:
                e["name"] = name
                e["role"] = role
                e["department"] = department
                break

        self.manager.write(employees)
