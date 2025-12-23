from models.punch_model import PunchModel
from datetime import datetime


class PunchController:
    def __init__(self):
        self.model = PunchModel()

    def register(self, employee_id, punch_type):
        punches = self.model.all()

        last = None
        for p in reversed(punches):
            if p["employee_id"] == employee_id:
                last = p
                break

        if last and last["type"] == punch_type:
            raise ValueError("Esse ponto já foi registrado.")

        punch = {
            "employee_id": employee_id,
            "type": punch_type,
            "timestamp": datetime.now().isoformat()
        }

        self.model.add(punch)

    def list_by_employee(self, employee_id):
        punches = self.model.all()
        return [p for p in punches if p["employee_id"] == employee_id]

    #STATUS ATUAL
    def get_current_status(self, employee_id):
        punches = self.list_by_employee(employee_id)

        if not punches:
            return "fora"

        last_type = punches[-1]["type"]

        if last_type in ("entrada", "retorno"):
            return "trabalhando"
        elif last_type == "intervalo":
            return "intervalo"
        else:
            return "fora"
