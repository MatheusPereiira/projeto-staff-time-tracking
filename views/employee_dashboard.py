from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox
)

from controllers.punch_controller import PunchController
from views.reports_view import ReportsView


class EmployeeDashboard(QWidget):
    def __init__(self, employee):
        super().__init__()

        self.employee = employee
        self.controller = PunchController()

        self.setWindowTitle("Registro de Ponto")
        self.setFixedSize(400, 420)

        layout = QVBoxLayout(self)

        label_employee = QLabel(f"Funcionário: {employee['name']}")
        label_user = QLabel(f"Usuário: {employee['user_username']}")

        layout.addWidget(label_employee)
        layout.addWidget(label_user)

        btn_entry = QPushButton("Entrada")
        btn_break = QPushButton("Intervalo")
        btn_return = QPushButton("Retorno")
        btn_exit = QPushButton("Saída")
        btn_report = QPushButton("Relatório de Horas")

        btn_entry.clicked.connect(lambda: self.register("entrada"))
        btn_break.clicked.connect(lambda: self.register("intervalo"))
        btn_return.clicked.connect(lambda: self.register("retorno"))
        btn_exit.clicked.connect(lambda: self.register("saida"))
        btn_report.clicked.connect(self.open_report)

        layout.addWidget(btn_entry)
        layout.addWidget(btn_break)
        layout.addWidget(btn_return)
        layout.addWidget(btn_exit)
        layout.addWidget(btn_report)

    def register(self, punch_type):
        try:
            self.controller.register(
                employee_id=self.employee["id"],
                punch_type=punch_type
            )
            QMessageBox.information(
                self,
                "Sucesso",
                f"Ponto registrado: {punch_type.capitalize()}"
            )
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def open_report(self):
        self.report_window = ReportsView(self.employee)
        self.report_window.show()
