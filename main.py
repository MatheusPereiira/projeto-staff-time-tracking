import sys
from PyQt6.QtWidgets import QApplication
from views.login_view import LoginView
from utils.bootstrap import create_admin_if_not_exists

# Cria admin padrão se não existir
create_admin_if_not_exists()

app = QApplication(sys.argv)

with open("assets/style.qss", "r", encoding="utf-8") as f:
    app.setStyleSheet(f.read())

window = LoginView()
window.show()

sys.exit(app.exec())
