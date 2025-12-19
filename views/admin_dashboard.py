from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget,
    QTableWidgetItem, QFrame
)
from PyQt6.QtCore import Qt

from controllers.employee_controller import EmployeeController
from controllers.report_controller import ReportController
from views.admin_reports_view import AdminReportsView


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard Administrativo")
        self.setMinimumSize(950, 550)

        self.employee_controller = EmployeeController()
        self.report_controller = ReportController()

        main_layout = QVBoxLayout(self)


        # TÍTULO

        title = QLabel("Dashboard Administrativo")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(title)


        # CARDS

        cards_layout = QHBoxLayout()
        metrics = self.report_controller.dashboard_metrics()

        cards_layout.addWidget(
            self.create_card("Funcionários", str(metrics["total_employees"]))
        )
        cards_layout.addWidget(
            self.create_card("Horas Totais", f'{metrics["total_hours"]} h')
        )
        cards_layout.addWidget(
            self.create_card("Média / Funcionário", f'{metrics["average_hours"]} h')
        )

        top = metrics["top_employee"]
        top_text = (
            f'{top["name"]}\n{top["hours"]} h'
            if top else "—"
        )

        cards_layout.addWidget(
            self.create_card("Destaque", top_text)
        )

        main_layout.addLayout(cards_layout)


        # BOTÕES

        btn_layout = QHBoxLayout()

        self.btn_reports = QPushButton("Relatórios")
        self.btn_refresh = QPushButton("Atualizar")

        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_reports)
        btn_layout.addWidget(self.btn_refresh)

        main_layout.addLayout(btn_layout)

        # TABELA
    
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([
            "Nome", "Cargo", "Departamento"
        ])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        main_layout.addWidget(self.table)

      
        # CONEXÕES
     
        self.btn_refresh.clicked.connect(self.load_data)
        self.btn_reports.clicked.connect(self.open_reports)

        self.load_data()

    def create_card(self, title: str, value: str) -> QFrame:
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-radius: 8px;
                padding: 12px;
            }
        """)

        layout = QVBoxLayout(card)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("font-size: 12px; color: #555;")

        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("font-size: 18px; font-weight: bold;")
        lbl_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)

        return card

    def load_data(self):
        self.table.setRowCount(0)
        employees = self.employee_controller.list_all()

        for row, emp in enumerate(employees):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(emp.get("name", "")))
            self.table.setItem(row, 1, QTableWidgetItem(emp.get("role", "")))
            self.table.setItem(row, 2, QTableWidgetItem(emp.get("department", "")))

    def open_reports(self):
        self.reports_window = AdminReportsView()
        self.reports_window.show()
