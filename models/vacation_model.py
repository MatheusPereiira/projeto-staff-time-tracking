from utils.json_manager import JsonManager

VAC_FILE = "data/vacations.json"

class VacationModel:
    def __init__(self):
        self.vacations = JsonManager.load(VAC_FILE, [])

    def add(self, employee_id, start, end):
        self.vacations.append({
            "employee_id": employee_id,
            "start": start,
            "end": end
        })
        JsonManager.save(VAC_FILE, self.vacations)
