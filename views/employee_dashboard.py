from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox
)

from controllers.punch_controller import PunchController
from views.reports_view import PunchHistoryView


class EmployeeDashboard(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.controller = PunchController()

        self.setWindowTitle("Registro de Ponto")
        self.setFixedSize(400, 350)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Funcionário: {user['username']}"))

        self.btn_entry = QPushButton("Entrada")
        self.btn_break = QPushButton("Intervalo")
        self.btn_return = QPushButton("Retorno")
        self.btn_exit = QPushButton("Saída")
        self.btn_history = QPushButton("Ver Histórico")

        self.btn_entry.clicked.connect(lambda: self.punch("entrada"))
        self.btn_break.clicked.connect(lambda: self.punch("intervalo"))
        self.btn_return.clicked.connect(lambda: self.punch("retorno"))
        self.btn_exit.clicked.connect(lambda: self.punch("saida"))
        self.btn_history.clicked.connect(self.open_history)

        layout.addWidget(self.btn_entry)
        layout.addWidget(self.btn_break)
        layout.addWidget(self.btn_return)
        layout.addWidget(self.btn_exit)
        layout.addWidget(self.btn_history)

        self.setLayout(layout)

    def punch(self, punch_type):
        try:
            self.controller.register(
                employee_id=self.user["username"],
                punch_type=punch_type
            )

            QMessageBox.information(
                self,
                "Sucesso",
                f"Ponto registrado: {punch_type.capitalize()}"
            )

        except ValueError as e:
            QMessageBox.warning(
                self,
                "Ação inválida",
                str(e)
            )

    def open_history(self):
        self.history_window = PunchHistoryView(self.user["username"])
        self.history_window.show()
