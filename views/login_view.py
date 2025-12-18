from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)

from controllers.auth_controller import AuthController
from controllers.employee_controller import EmployeeController
from views.admin_dashboard import AdminDashboard
from views.employee_dashboard import EmployeeDashboard


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.auth = AuthController()
        self.employee_controller = EmployeeController()

        self.setWindowTitle("Folha de Ponto - Login")
        self.setFixedSize(300, 220)

        layout = QVBoxLayout()

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuário")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Senha")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn = QPushButton("Entrar")
        btn.clicked.connect(self.login)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.user_input)
        layout.addWidget(self.password_input)
        layout.addWidget(btn)

        self.setLayout(layout)

    def login(self):
        username = self.user_input.text().strip()
        password = self.password_input.text().strip()

        user = self.auth.login(username, password)

        if not user:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos")
            return

        # 🔐 ADMIN
        if user["role"] == "admin":
            QMessageBox.information(self, "Sucesso", "Bem-vindo, administrador!")
            self.dashboard = AdminDashboard()
            self.dashboard.show()
            self.close()
            return

        # 👤 FUNCIONÁRIO
        employee = self.employee_controller.get_by_username(username)

        if not employee:
            QMessageBox.warning(
                self,
                "Erro",
                "Usuário válido, mas funcionário não cadastrado"
            )
            return

        QMessageBox.information(
            self,
            "Sucesso",
            f"Bem-vindo, {employee['name']}!"
        )

        self.dashboard = EmployeeDashboard(employee)
        self.dashboard.show()
        self.close()
