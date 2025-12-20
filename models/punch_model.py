from utils.json_manager import JsonManager
from datetime import datetime


class PunchModel:
    def __init__(self):
        self.db = JsonManager("punches.json")

    def all(self):
        return self.db.read()

    def add(self, punch: dict):
        data = self.db.read()
        data.append(punch)
        self.db.write(data)

    def by_employee(self, employee_id: str, start=None, end=None):
        punches = [
            p for p in self.db.read()
            if p["employee_id"] == employee_id
        ]

        if start and end:
            start_dt = datetime.fromisoformat(start)
            end_dt = datetime.fromisoformat(end)

            punches = [
                p for p in punches
                if start_dt <= datetime.fromisoformat(p["timestamp"]) <= end_dt
            ]

        return punches
