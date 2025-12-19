from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton, QHBoxLayout,
    QFileDialog, QMessageBox, QHeaderView
)
from PyQt6.QtCore import Qt

from controllers.report_controller import ReportController


class AdminReportsView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Relatório Administrativo")
        self.setFixedSize(900, 500)

        self.controller = ReportController()

        layout = QVBoxLayout()

        title = QLabel("Relatório de Horas Trabalhadas")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        # Tabela
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([
            "Nome", "Usuário", "Horas Trabalhadas"
        ])

        # Ajuste correto das colunas
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        layout.addWidget(self.table)

        # Botões
        btn_layout = QHBoxLayout()

        btn_csv = QPushButton("Exportar CSV")
        btn_pdf = QPushButton("Exportar PDF")

        btn_csv.clicked.connect(self.export_csv)
        btn_pdf.clicked.connect(self.export_pdf)

        btn_layout.addWidget(btn_csv)
        btn_layout.addWidget(btn_pdf)

        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        data = self.controller.admin_summary()
        self.table.setRowCount(len(data))

        for row, item in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(item["username"]))

            hours_item = QTableWidgetItem(str(item["hours"]))
            hours_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 2, hours_item)

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar CSV", "", "CSV Files (*.csv)"
        )
        if not path:
            return

        try:
            self.controller.export_csv(path)
            QMessageBox.information(self, "Sucesso", "Relatório CSV exportado.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    def export_pdf(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar PDF", "", "PDF Files (*.pdf)"
        )
        if not path:
            return

        try:
            self.controller.export_pdf(path)
            QMessageBox.information(self, "Sucesso", "Relatório PDF exportado.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))
