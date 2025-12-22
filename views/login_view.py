from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)

from controllers.auth_controller import AuthController
from controllers.employee_controller import EmployeeController
from views.admin_dashboard import AdminDashboard
from views.employee_dashboard import EmployeeDashboard


class LoginView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(360, 260)

        self.auth_controller = AuthController()
        self.employee_controller = EmployeeController()

        layout = QVBoxLayout(self)

        title = QLabel("Acesso ao Sistema")
        title.setObjectName("LoginTitle")

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Usuário")

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Senha")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Entrar")
        btn_login.clicked.connect(self.login)

        layout.addWidget(title)
        layout.addWidget(self.input_username)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)

    def login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        user = self.auth_controller.login(username, password)

        if not user:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos")
            return

        if user["role"] == "admin":
            self.dashboard = AdminDashboard()
            self.dashboard.show()
            self.close()
            return

        employee = self.employee_controller.get_by_username(username)

        if not employee:
            QMessageBox.warning(
                self,
                "Erro",
                "Usuário válido, mas funcionário não cadastrado"
            )
            return

        self.dashboard = EmployeeDashboard(employee)
        self.dashboard.show()
        self.close()
