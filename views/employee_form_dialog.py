from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)

from controllers.employee_controller import EmployeeController


class EmployeeFormDialog(QDialog):
    def __init__(self, parent=None, employee=None):
        super().__init__(parent)

        self.employee = employee
        self.controller = EmployeeController()

        self.setFixedSize(400, 260)
        self.setWindowTitle(
            "Editar Funcionário" if employee else "Novo Funcionário"
        )

        self.init_ui()

        if self.employee:
            self.fill_form()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        title = QLabel(
            "Editar Funcionário" if self.employee else "Cadastrar Funcionário"
        )
        title.setObjectName("DialogTitle")
        layout.addWidget(title)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nome do funcionário")
        layout.addWidget(self.input_name)

        self.input_role = QLineEdit()
        self.input_role.setPlaceholderText("Cargo")
        layout.addWidget(self.input_role)

        self.input_department = QLineEdit()
        self.input_department.setPlaceholderText("Departamento")
        layout.addWidget(self.input_department)

        buttons = QHBoxLayout()
        buttons.addStretch()

        btn_cancel = QPushButton("Cancelar")
        btn_cancel.clicked.connect(self.reject)

        btn_save = QPushButton("Salvar")
        btn_save.clicked.connect(self.save)

        buttons.addWidget(btn_cancel)
        buttons.addWidget(btn_save)
        layout.addLayout(buttons)

    def fill_form(self):
        self.input_name.setText(self.employee["name"])
        self.input_role.setText(self.employee["role"])
        self.input_department.setText(self.employee["department"])

    def save(self):
        name = self.input_name.text().strip()
        role = self.input_role.text().strip()
        department = self.input_department.text().strip()

        if not name or not role or not department:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        data = {
            "name": name,
            "role": role,
            "department": department
        }

        if self.employee:
            self.controller.update(self.employee["id"], data)
        else:
            self.controller.create(data)

        self.accept()
