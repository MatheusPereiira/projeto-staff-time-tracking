from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QTableWidget,
    QTableWidgetItem, QMessageBox
)

from controllers.employee_controller import EmployeeController
from views.admin_reports_view import AdminReportsView


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard Administrativo")
        self.setMinimumSize(900, 500)

        self.controller = EmployeeController()

        main_layout = QVBoxLayout()

        #TÍTULO 
        title = QLabel("Funcionários")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(title)

        #BOTÕES
        btn_layout = QHBoxLayout()

        self.btn_new = QPushButton("Novo")
        self.btn_edit = QPushButton("Editar")
        self.btn_delete = QPushButton("Excluir")
        self.btn_refresh = QPushButton("Atualizar")
        self.btn_reports = QPushButton("Relatórios")

        btn_layout.addWidget(self.btn_new)
        btn_layout.addWidget(self.btn_edit)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_reports)
        btn_layout.addWidget(self.btn_refresh)

        main_layout.addLayout(btn_layout)

        #TABELA
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([
            "Nome", "Cargo", "Departamento"
        ])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

        #CONEXÕES
        self.btn_refresh.clicked.connect(self.load_data)
        self.btn_reports.clicked.connect(self.open_reports)
        self.load_data()

    #MÉTODOS 
    def load_data(self):
        self.table.setRowCount(0)
        employees = self.controller.list_all()

        for row, emp in enumerate(employees):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(emp.get("name", "")))
            self.table.setItem(row, 1, QTableWidgetItem(emp.get("role", "")))
            self.table.setItem(row, 2, QTableWidgetItem(emp.get("department", "")))

    def open_reports(self):
        self.reports_window = AdminReportsView()
        self.reports_window.show()
