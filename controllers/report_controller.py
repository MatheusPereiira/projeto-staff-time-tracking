from models.punch_model import PunchModel
from utils.datetime_utils import diff_hours

class ReportController:
    def __init__(self):
        self.model = PunchModel()

    def total_hours(self, employee_id):
        punches = self.model.by_employee(employee_id)
        total = 0

        for i in range(0, len(punches) - 1, 2):
            total += diff_hours(
                punches[i]["timestamp"],
                punches[i + 1]["timestamp"]
            )

        return round(total, 2)
