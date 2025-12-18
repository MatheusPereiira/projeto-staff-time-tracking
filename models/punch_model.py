from utils.json_manager import JSONManager
from utils.datetime_utils import now_iso


class PunchModel:
    def __init__(self):
        self.db = JSONManager("punches.json")

    def all(self) -> list:
        return self.db.read()

    def add(self, punch: dict):
        punches = self.all()
        punches.append(punch)
        self.db.write(punches)

    def by_employee(self, employee_id: str) -> list:
        return [
            p for p in self.all()
            if p["employee_id"] == employee_id
        ]

    def register(self, employee_id: str, punch_type: str):
        self.add({
            "employee_id": employee_id,
            "type": punch_type,
            "timestamp": now_iso()
        })
