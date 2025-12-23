from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QPushButton,
    QMessageBox, QHBoxLayout
)

from controllers.employee_controller import EmployeeController
from models.user_model import UserModel


class EmployeeFormDialog(QDialog):
    def __init__(self, parent=None, employee=None):
        super().__init__(parent)

        self.employee = employee
        self.employee_controller = EmployeeController()
        self.user_model = UserModel()

        self.setWindowTitle(
            "Editar Funcionário" if self.employee else "Novo Funcionário"
        )
        self.setFixedWidth(420)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nome")

        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("Cargo")

        self.department_input = QLineEdit()
        self.department_input.setPlaceholderText("Departamento")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuário")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Nova senha (opcional)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Se for edição, preenche campos
        if self.employee:
            self.name_input.setText(self.employee.get("name", ""))
            self.role_input.setText(self.employee.get("role", ""))
            self.department_input.setText(self.employee.get("department", ""))
            self.username_input.setText(self.employee.get("user_username", ""))

        btn_layout = QHBoxLayout()

        cancel_btn = QPushButton("Cancelar")
        save_btn = QPushButton("Salvar")

        cancel_btn.clicked.connect(self.reject)
        save_btn.clicked.connect(self.save)

        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)

        layout.addWidget(self.name_input)
        layout.addWidget(self.role_input)
        layout.addWidget(self.department_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addLayout(btn_layout)

    def save(self):
        name = self.name_input.text().strip()
        role = self.role_input.text().strip()
        department = self.department_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not name or not role or not department or not username:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos obrigatórios.")
            return

        # EDITAR
        if self.employee:
            self.employee_controller.update(
                self.employee["id"],
                {
                    "name": name,
                    "role": role,
                    "department": department
                }
            )

            if password:
                self.user_model.update_password(username, password)

        # NOVO
        else:
            self.employee_controller.create(
                name=name,
                role=role,
                department=department,
                username=username,
                password=password or "123456"
            )

        QMessageBox.information(self, "Sucesso", "Funcionário salvo com sucesso.")
        self.accept()
