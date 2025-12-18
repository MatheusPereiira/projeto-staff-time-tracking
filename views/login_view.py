from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)

from controllers.auth_controller import AuthController
from views.admin_dashboard import AdminDashboard
from views.employee_dashboard import EmployeeDashboard


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.auth = AuthController()
        self.setWindowTitle("Folha de Ponto - Login")
        self.setFixedSize(300, 220)

        layout = QVBoxLayout()

        self.user = QLineEdit()
        self.user.setPlaceholderText("Usuário")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Senha")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        btn = QPushButton("Entrar")
        btn.clicked.connect(self.login)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.user)
        layout.addWidget(self.password)
        layout.addWidget(btn)

        self.setLayout(layout)

    def login(self):
        user = self.auth.login(self.user.text(), self.password.text())

        if not user:
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos")
            return

        QMessageBox.information(
            self,
            "Sucesso",
            f"Bem-vindo! Perfil: {user['role']}"
        )

        # 🔀 REDIRECIONAMENTO CORRETO
        if user["role"] == "admin":
            self.dashboard = AdminDashboard()
        else:
            self.dashboard = EmployeeDashboard(user)

        self.dashboard.show()
        self.close()
