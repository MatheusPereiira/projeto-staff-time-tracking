from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLabel
)
from controllers.punch_controller import PunchController
from utils.datetime_utils import format_br


class PunchHistoryView(QWidget):
    def __init__(self, employee_id):
        super().__init__()
        self.setWindowTitle("Histórico de Ponto")
        self.setFixedSize(600, 400)

        controller = PunchController()
        punches = controller.history(employee_id)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Histórico de Registros"))

        table = QTableWidget(len(punches), 3)
        table.setHorizontalHeaderLabels([
            "Tipo", "Data / Hora", "Funcionário"
        ])

        for row, punch in enumerate(punches):
            table.setItem(row, 0, QTableWidgetItem(punch["type"].capitalize()))
            table.setItem(
                row,
                1,
                QTableWidgetItem(format_br(punch["timestamp"]))
            )
            table.setItem(row, 2, QTableWidgetItem(punch["employee_id"]))

        layout.addWidget(table)
        self.setLayout(layout)
