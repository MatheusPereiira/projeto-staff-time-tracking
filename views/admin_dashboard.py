from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QDateEdit
)
from PyQt6.QtCore import QDate

from controllers.employee_controller import EmployeeController
from controllers.report_controller import ReportController
from views.admin_reports_view import AdminReportsView


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Administrativo")
        self.resize(1100, 650)

        self.employee_controller = EmployeeController()
        self.report_controller = ReportController()

        self.init_ui()
        self.load_data()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(24, 24, 24, 24)

        title = QLabel("Dashboard Administrativo")
        title.setObjectName("DashboardTitle")
        main_layout.addWidget(title)

        #FILTROS
        filter_layout = QHBoxLayout()

        self.start_date = QDateEdit(QDate.currentDate().addMonths(-1))
        self.start_date.setCalendarPopup(True)

        self.end_date = QDateEdit(QDate.currentDate())
        self.end_date.setCalendarPopup(True)

        btn_filter = QPushButton("Aplicar Filtro")
        btn_filter.clicked.connect(self.load_data)

        filter_layout.addWidget(QLabel("De:"))
        filter_layout.addWidget(self.start_date)
        filter_layout.addWidget(QLabel("Até:"))
        filter_layout.addWidget(self.end_date)
        filter_layout.addWidget(btn_filter)
        filter_layout.addStretch()

        main_layout.addLayout(filter_layout)

        #CARDS
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(20)

        self.card_employees = self.create_card(
            "Funcionários", "Ativos no sistema"
        )
        self.card_total_hours = self.create_card(
            "Horas Totais", "Período filtrado"
        )
        self.card_average = self.create_card(
            "Média / Funcionário", "Horas médias"
        )
        self.card_highlight = self.create_highlight_card(
            "Destaque", "Maior carga horária"
        )

        cards_layout.addWidget(self.card_employees)
        cards_layout.addWidget(self.card_total_hours)
        cards_layout.addWidget(self.card_average)
        cards_layout.addWidget(self.card_highlight)

        main_layout.addLayout(cards_layout)

        #TABELA
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["Nome", "Cargo", "Departamento"]
        )

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)

        main_layout.addWidget(self.table)

    def create_card(self, title_text, subtitle_text):
        card = QWidget()
        card.setObjectName("Card")
        layout = QVBoxLayout(card)

        title = QLabel(title_text)
        title.setObjectName("CardTitle")

        value = QLabel("0")
        value.setObjectName("CardValue")

        subtitle = QLabel(subtitle_text)
        subtitle.setObjectName("CardSubtitle")

        layout.addWidget(title)
        layout.addWidget(value)
        layout.addWidget(subtitle)

        card.value_label = value
        return card

    def create_highlight_card(self, title_text, subtitle_text):
        card = QWidget()
        card.setObjectName("HighlightCard")
        layout = QVBoxLayout(card)

        title = QLabel(title_text)
        title.setObjectName("CardTitle")

        value = QLabel("-")
        value.setObjectName("CardValue")

        subtitle = QLabel(subtitle_text)
        subtitle.setObjectName("CardSubtitle")

        layout.addWidget(title)
        layout.addWidget(value)
        layout.addWidget(subtitle)

        card.value_label = value
        return card

    def load_data(self):
        start = self.start_date.date().toString("yyyy-MM-dd")
        end = self.end_date.date().toString("yyyy-MM-dd")

        employees = self.employee_controller.all()
        summary = self.report_controller.admin_summary(start, end)

        total_employees = len(employees)
        total_hours = sum(item["hours"] for item in summary)
        avg_hours = (
            total_hours / total_employees
            if total_employees > 0 else 0
        )

        highlight = max(summary, key=lambda x: x["hours"], default=None)

        self.card_employees.value_label.setText(str(total_employees))
        self.card_total_hours.value_label.setText(f"{total_hours:.1f} h")
        self.card_average.value_label.setText(f"{avg_hours:.1f} h")

        if highlight:
            self.card_highlight.value_label.setText(
                f'{highlight["name"]} — {highlight["hours"]:.1f} h'
            )
        else:
            self.card_highlight.value_label.setText("-")

        self.table.setRowCount(len(summary))
        for row, emp in enumerate(summary):
            self.table.setItem(row, 0, QTableWidgetItem(emp["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(emp["role"]))
            self.table.setItem(row, 2, QTableWidgetItem(emp["department"]))

    def open_reports(self):
        self.reports_window = AdminReportsView()
        self.reports_window.show()
