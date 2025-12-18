from models.punch_model import PunchModel
from utils.datetime_utils import diff_hours


class ReportController:
    def __init__(self):
        self.model = PunchModel()

    def hours_by_employee(self, employee_id: str):
        punches = self.model.by_employee(employee_id)

        total_hours = 0.0
        last_entry = None

        for punch in punches:
            if punch["type"] == "entrada":
                last_entry = punch["timestamp"]

            elif punch["type"] == "saida" and last_entry:
                total_hours += diff_hours(last_entry, punch["timestamp"])
                last_entry = None

        return round(total_hours, 2)
