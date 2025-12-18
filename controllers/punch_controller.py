from models.punch_model import PunchModel

class PunchController:
    def __init__(self):
        self.model = PunchModel()

    def register(self, employee_id, punch_type):
        self.model.register(employee_id, punch_type)

    def history(self, employee_id):
        return self.model.by_employee(employee_id)
