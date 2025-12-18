from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QHBoxLayout, QPushButton,
    QComboBox, QDateEdit, QFrame
)
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QFont
from controllers.punch_controller import PunchController
from datetime import datetime


class ReportsView(QWidget):
    def __init__(self, employee):
        super().__init__()

        self.employee = employee
        self.controller = PunchController()

        self.setWindowTitle("Histórico de Pontos")
        self.setFixedSize(700, 460)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        #TÍTULO
        title = QLabel("Histórico de Pontos")
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        main_layout.addWidget(title)

        subtitle = QLabel(f"Funcionário: {employee['name']}")
        subtitle.setFont(QFont("Segoe UI", 10))
        main_layout.addWidget(subtitle)

        #CARD DE FILTROS
        filter_card = QFrame()
        filter_card.setObjectName("filterCard")
        filter_layout = QHBoxLayout(filter_card)
        filter_layout.setSpacing(10)

        self.type_filter = QComboBox()
        self.type_filter.addItems(
            ["todos", "entrada", "intervalo", "retorno", "saida"]
        )

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate.currentDate().addMonths(-1))

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QDate.currentDate())

        btn_filter = QPushButton("Filtrar")
        btn_filter.setFixedHeight(32)
        btn_filter.clicked.connect(self.load_data)

        filter_layout.addWidget(QLabel("Tipo:"))
        filter_layout.addWidget(self.type_filter)
        filter_layout.addWidget(QLabel("De:"))
        filter_layout.addWidget(self.start_date)
        filter_layout.addWidget(QLabel("Até:"))
        filter_layout.addWidget(self.end_date)
        filter_layout.addStretch()
        filter_layout.addWidget(btn_filter)

        main_layout.addWidget(filter_card)

        #TABELA
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Data", "Hora", "Tipo"])
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.verticalHeader().setVisible(False)

        header_font = QFont("Segoe UI", 10, QFont.Weight.Bold)
        self.table.horizontalHeader().setFont(header_font)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)

        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)

        punches = self.controller.filter_punches(
            employee_id=self.employee["id"],
            punch_type=self.type_filter.currentText(),
            start_date=self.start_date.date().toPyDate(),
            end_date=self.end_date.date().toPyDate()
        )

        for punch in punches:
            row = self.table.rowCount()
            self.table.insertRow(row)

            dt = datetime.fromisoformat(punch["timestamp"])

            item_date = QTableWidgetItem(dt.strftime("%d/%m/%Y"))
            item_time = QTableWidgetItem(dt.strftime("%H:%M:%S"))
            item_type = QTableWidgetItem(punch["type"].capitalize())

            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_time.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_type.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table.setItem(row, 0, item_date)
            self.table.setItem(row, 1, item_time)
            self.table.setItem(row, 2, item_type)
