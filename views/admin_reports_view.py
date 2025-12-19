from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem,
    QPushButton
)
from PyQt6.QtCore import Qt
from controllers.report_controller import ReportController
from datetime import datetime


class AdminReportsView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Relatórios Administrativos")
        self.setFixedSize(700, 450)

        self.controller = ReportController()

        layout = QVBoxLayout()

        title = QLabel("Relatório Geral de Pontos")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Funcionário", "Data", "Hora", "Tipo"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.table)

        btn_refresh = QPushButton("Atualizar Relatório")
        btn_refresh.clicked.connect(self.load_data)
        layout.addWidget(btn_refresh)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        reports = self.controller.list_all()
        self.table.setRowCount(len(reports))

        for row, r in enumerate(reports):
            dt = datetime.fromisoformat(r["timestamp"])
            date_str = dt.strftime("%d/%m/%Y")
            time_str = dt.strftime("%H:%M:%S")

            self.table.setItem(row, 0, QTableWidgetItem(r["employee"]))
            self.table.setItem(row, 1, QTableWidgetItem(date_str))
            self.table.setItem(row, 2, QTableWidgetItem(time_str))
            self.table.setItem(row, 3, QTableWidgetItem(r["type"]))
