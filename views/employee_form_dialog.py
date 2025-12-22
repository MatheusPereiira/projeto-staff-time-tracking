from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)

from controllers.employee_controller import EmployeeController


class EmployeeFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Novo Funcionário")
        self.setFixedSize(420, 360)

        self.controller = EmployeeController()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nome do funcionário")

        self.input_role = QLineEdit()
        self.input_role.setPlaceholderText("Cargo")

        self.input_department = QLineEdit()
        self.input_department.setPlaceholderText("Departamento")

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Usuário de acesso")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Senha inicial")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.input_name)
        layout.addWidget(self.input_role)
        layout.addWidget(self.input_department)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)

        buttons = QHBoxLayout()

        btn_cancel = QPushButton("Cancelar")
        btn_cancel.clicked.connect(self.reject)

        btn_save = QPushButton("Salvar")
        btn_save.clicked.connect(self.save)

        buttons.addWidget(btn_cancel)
        buttons.addWidget(btn_save)

        layout.addLayout(buttons)

    def save(self):
        name = self.input_name.text().strip()
        role = self.input_role.text().strip()
        department = self.input_department.text().strip()
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if not all([name, role, department, username, password]):
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        self.controller.create_with_user({
            "name": name,
            "role": role,
            "department": department,
            "username": username,
            "password": password
        })

        QMessageBox.information(
            self,
            "Sucesso",
            "Funcionário e usuário criados com sucesso!"
        )

        self.accept()
