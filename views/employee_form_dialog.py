from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)

from controllers.employee_controller import EmployeeController


class EmployeeFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = EmployeeController()

        self.setWindowTitle("Novo Funcionário")
        self.setFixedSize(420, 360)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Nome do Funcionário"))
        self.name = QLineEdit()
        layout.addWidget(self.name)

        layout.addWidget(QLabel("Cargo"))
        self.role = QLineEdit()
        layout.addWidget(self.role)

        layout.addWidget(QLabel("Departamento"))
        self.department = QLineEdit()
        layout.addWidget(self.department)

        layout.addWidget(QLabel("Usuário de Acesso"))
        self.username = QLineEdit()
        layout.addWidget(self.username)

        layout.addWidget(QLabel("Senha Inicial"))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        buttons = QHBoxLayout()
        btn_cancel = QPushButton("Cancelar")
        btn_cancel.clicked.connect(self.reject)

        btn_save = QPushButton("Salvar")
        btn_save.clicked.connect(self.save)

        buttons.addWidget(btn_cancel)
        buttons.addWidget(btn_save)
        layout.addLayout(buttons)

    def save(self):
        if not all([
            self.name.text().strip(),
            self.role.text().strip(),
            self.department.text().strip(),
            self.username.text().strip(),
            self.password.text().strip()
        ]):
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        try:
            self.controller.create_with_user({
                "name": self.name.text().strip(),
                "role": self.role.text().strip(),
                "department": self.department.text().strip(),
                "username": self.username.text().strip(),
                "password": self.password.text().strip()
            })
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))
            return

        QMessageBox.information(self, "Sucesso", "Funcionário cadastrado com sucesso!")
        self.accept()
