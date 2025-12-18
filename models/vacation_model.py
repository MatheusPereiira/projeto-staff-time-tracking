from utils.json_manager import JSONManager

VAC_FILE = "data/vacations.json"

class VacationModel:
    def __init__(self):
        self.vacations = JSONManager.load(VAC_FILE, [])

    def add(self, employee_id, start, end):
        self.vacations.append({
            "employee_id": employee_id,
            "start": start,
            "end": end
        })
        JSONManager.save(VAC_FILE, self.vacations)
