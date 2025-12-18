from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt6.QtCore import Qt
from datetime import datetime

from controllers.punch_controller import PunchController


class ReportsView(QWidget):
    def __init__(self, employee):
        super().__init__()

        self.employee = employee
        self.controller = PunchController()

        self.setWindowTitle("Relatório de Horas Trabalhadas")
        self.setFixedSize(360, 240)

        layout = QVBoxLayout()

        title = QLabel("Relatório de Horas")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:18px; font-weight:bold;")

        name = QLabel(f"Funcionário: {employee['name']}")
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        total_hours = self.calculate_hours()

        hours_label = QLabel(
            f"Total de horas trabalhadas:\n{total_hours:.2f} h"
        )
        hours_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hours_label.setStyleSheet("font-size:16px;")

        btn_close = QPushButton("Fechar")
        btn_close.clicked.connect(self.close)

        layout.addWidget(title)
        layout.addWidget(name)
        layout.addSpacing(10)
        layout.addWidget(hours_label)
        layout.addStretch()
        layout.addWidget(btn_close)

        self.setLayout(layout)

    def calculate_hours(self):
        punches = self.controller.list_by_employee(self.employee["id"])

        total_hours = 0.0
        entrada = None

        for punch in punches:
            time = datetime.fromisoformat(punch["timestamp"])

            if punch["type"] == "entrada":
                entrada = time

            elif punch["type"] == "saida" and entrada:
                diff = time - entrada
                total_hours += diff.total_seconds() / 3600
                entrada = None

        return total_hours
