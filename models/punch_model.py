from utils.json_manager import JSONManager


class PunchModel:
    def __init__(self):
        self.db = JSONManager("punches.json")

    def all(self):
        return self.db.read()

    def add(self, punch: dict):
        data = self.db.read()
        data.append(punch)
        self.db.write(data)

    def by_employee(self, employee_id: str):
        return [
            p for p in self.db.read()
            if p["employee_id"] == employee_id
        ]
