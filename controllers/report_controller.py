import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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


    # DADOS PARA O DASHBOARD
 
    def dashboard_metrics(self):
        data = self.admin_summary()

        total_employees = len(data)
        total_hours = sum(item["hours"] for item in data)
        avg_hours = round(total_hours / total_employees, 2) if total_employees else 0

        top_employee = max(data, key=lambda x: x["hours"], default=None)

        return {
            "total_employees": total_employees,
            "total_hours": round(total_hours, 2),
            "average_hours": avg_hours,
            "top_employee": top_employee
        }

    # EXPORTAÇÕES
    def export_csv(self, file_path: str):
        data = self.admin_summary()

        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Usuário", "Horas Trabalhadas"])

            for row in data:
                writer.writerow([
                    row["name"],
                    row["username"],
                    row["hours"]
                ])

    def export_pdf(self, file_path: str):
        data = self.admin_summary()

        c = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4

        y = height - 50
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Relatório de Horas Trabalhadas")

        y -= 30
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Nome")
        c.drawString(250, y, "Usuário")
        c.drawString(400, y, "Horas")

        y -= 15
        c.setFont("Helvetica", 10)

        for row in data:
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 10)

            c.drawString(50, y, row["name"])
            c.drawString(250, y, row["username"])
            c.drawString(400, y, str(row["hours"]))
            y -= 15

        c.save()
