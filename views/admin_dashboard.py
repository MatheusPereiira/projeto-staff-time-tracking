from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox,
    QDialog, QLabel, QLineEdit, QFormLayout
)
from PyQt6.QtCore import Qt

from controllers.employee_controller import EmployeeController


class EmployeeForm(QDialog):
    def __init__(self, employee=None):
        super().__init__()
        self.setWindowTitle("Funcionário")
        self.setFixedSize(300, 200)
        self.employee = employee

        layout = QFormLayout()

        self.name = QLineEdit()
        self.role = QLineEdit()
        self.department = QLineEdit()

        if employee:
            self.name.setText(employee["name"])
            self.role.setText(employee["role"])
            self.department.setText(employee["department"])

        btn_save = QPushButton("Salvar")
        btn_save.clicked.connect(self.accept)

        layout.addRow("Nome:", self.name)
        layout.addRow("Cargo:", self.role)
        layout.addRow("Departamento:", self.department)
        layout.addWidget(btn_save)

        self.setLayout(layout)

    def data(self):
        return self.name.text(), self.role.text(), self.department.text()


class AdminDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard Administrativo")
        self.setFixedSize(800, 500)

        self.controller = EmployeeController()
        self.selected_employee = None

        main_layout = QVBoxLayout()
        toolbar = QHBoxLayout()

        btn_add = QPushButton("Novo")
        btn_edit = QPushButton("Editar")
        btn_delete = QPushButton("Excluir")
        btn_refresh = QPushButton("Atualizar")

        btn_add.clicked.connect(self.add_employee)
        btn_edit.clicked.connect(self.edit_employee)
        btn_delete.clicked.connect(self.delete_employee)
        btn_refresh.clicked.connect(self.load_table)

        toolbar.addWidget(btn_add)
        toolbar.addWidget(btn_edit)
        toolbar.addWidget(btn_delete)
        toolbar.addStretch()
        toolbar.addWidget(btn_refresh)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nome", "Cargo", "Departamento"])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.cellClicked.connect(self.select_row)
        self.table.doubleClicked.connect(self.edit_employee)

        main_layout.addWidget(QLabel("Funcionários"))
        main_layout.addLayout(toolbar)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)
        self.load_table()

    def load_table(self):
        employees = self.controller.list_all()
        self.table.setRowCount(len(employees))
        self.selected_employee = None

        for row, emp in enumerate(employees):
            self.table.setItem(row, 0, QTableWidgetItem(emp["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(emp["role"]))
            self.table.setItem(row, 2, QTableWidgetItem(emp["department"]))

    def select_row(self, row):
        self.selected_employee = self.controller.list_all()[row]

    def add_employee(self):
        dialog = EmployeeForm()
        if dialog.exec():
            name, role, dept = dialog.data()
            self.controller.create(name, role, dept)
            self.load_table()

    def edit_employee(self):
        if not self.selected_employee:
            QMessageBox.warning(self, "Aviso", "Selecione um funcionário")
            return

        dialog = EmployeeForm(self.selected_employee)
        if dialog.exec():
            name, role, dept = dialog.data()
            self.selected_employee.update({
                "name": name,
                "role": role,
                "department": dept
            })
            self.controller.model.save()
            self.load_table()

    def delete_employee(self):
        if not self.selected_employee:
            QMessageBox.warning(self, "Aviso", "Selecione um funcionário")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmação",
            "Deseja excluir este funcionário?"
        )

        if confirm == QMessageBox.StandardButton.Yes:
            self.controller.model.employees.remove(self.selected_employee)
            self.controller.model.save()
            self.load_table()
