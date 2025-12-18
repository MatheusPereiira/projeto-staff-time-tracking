from models.punch_model import PunchModel
from datetime import datetime


class PunchController:
    def __init__(self):
        self.model = PunchModel()

    def register(self, employee_id, punch_type):
        punches = self.model.by_employee(employee_id)

        last = punches[-1] if punches else None

        if last and last["type"] == punch_type:
            raise ValueError("Esse ponto já foi registrado.")

        punch = {
            "employee_id": employee_id,
            "type": punch_type,
            "timestamp": datetime.now().isoformat()
        }

        self.model.add(punch)

    def list_by_employee(self, employee_id):
        return self.model.by_employee(employee_id)

    #FILTRO DE PONTOS
    def filter_punches(
        self,
        employee_id,
        punch_type=None,
        start_date=None,
        end_date=None
    ):
        punches = self.model.by_employee(employee_id)
        result = []

        for p in punches:
            punch_date = datetime.fromisoformat(p["timestamp"])

            if punch_type and punch_type != "todos":
                if p["type"] != punch_type:
                    continue

            if start_date and punch_date.date() < start_date:
                continue

            if end_date and punch_date.date() > end_date:
                continue

            result.append(p)

        return result
