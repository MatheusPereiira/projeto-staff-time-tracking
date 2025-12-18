from models.employee_model import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.model = EmployeeModel()

    def list_all(self):
        """
        Retorna todos os funcionários
        """
        return self.model.all()

    def create(self, name, role, department):
        """
        Cria um novo funcionário
        """
        return self.model.add(name, role, department)

    def update(self, employee_id, name, role, department):
        """
        Atualiza um funcionário existente
        """
        self.model.update(employee_id, name, role, department)

    def delete(self, employee_id):
        """
        Remove um funcionário
        """
        self.model.delete(employee_id)
