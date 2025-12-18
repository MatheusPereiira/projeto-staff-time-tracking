from models.user_model import UserModel
from utils.security import hash_password


def create_admin_if_not_exists():
    model = UserModel()
    users = model.all()

    for user in users:
        if user["username"] == "admin":
            return

    admin = {
        "username": "admin",
        "password": hash_password("admin123"),
        "role": "admin"
    }

    model.add(admin)
