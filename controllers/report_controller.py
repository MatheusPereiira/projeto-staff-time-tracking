from models.punch_model import PunchModel
from models.employee_model import EmployeeModel
from utils.datetime_utils import diff_hours


class ReportController:
    def __init__(self):
        self.punch_model = PunchModel()
        self.employee_model = EmployeeModel()

    def hours_by_employee(self, employee_id: str):
        punches = self.punch_model.by_employee(employee_id)

        total_hours = 0.0
        last_entry = None

        for punch in punches:
            if punch["type"] == "entrada":
                last_entry = punch["timestamp"]

            elif punch["type"] == "saida" and last_entry:
                total_hours += diff_hours(
                    last_entry,
                    punch["timestamp"]
                )
                last_entry = None

        return round(total_hours, 2)


    def admin_summary(self):
        result = []

        for emp in self.employee_model.all():
            total = self.hours_by_employee(emp["id"])

            result.append({
                "name": emp["name"],
                "username": emp.get("username", ""),
                "hours": total
            })

        return result

    def list_all(self):
        punches = self.punch_model.all()
        employees = self.employee_model.all()

        emp_map = {e["id"]: e["name"] for e in employees}

        reports = []
        for p in punches:
            reports.append({
                "employee": emp_map.get(p["employee_id"], "Desconhecido"),
                "type": p["type"].capitalize(),
                "timestamp": p["timestamp"]
            })

        return reports
