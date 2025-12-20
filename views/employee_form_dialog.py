from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

from controllers.employee_controller import EmployeeController


class EmployeeFormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Novo Funcionário")
        self.setFixedSize(400, 260)

        self.controller = EmployeeController()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # TÍTULO
        title = QLabel("Cadastrar Funcionário")
        title.setObjectName("DialogTitle")
        layout.addWidget(title)

        #  NOME 
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nome do funcionário")
        layout.addWidget(self.input_name)

        # CARGO
        self.input_role = QLineEdit()
        self.input_role.setPlaceholderText("Cargo")
        layout.addWidget(self.input_role)

        #DEPARTAMENTO 
        self.input_department = QLineEdit()
        self.input_department.setPlaceholderText("Departamento")
        layout.addWidget(self.input_department)

        # BOTÕES 
        buttons = QHBoxLayout()
        buttons.addStretch()

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

        if not name or not role or not department:
            QMessageBox.warning(
                self,
                "Erro",
                "Preencha todos os campos."
            )
            return

        self.controller.create({
            "name": name,
            "role": role,
            "department": department
        })

        QMessageBox.information(
            self,
            "Sucesso",
            "Funcionário cadastrado com sucesso!"
        )

        self.accept()
