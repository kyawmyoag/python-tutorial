from employee.base_employee import EmployeeBase

class ProbationEmployee(EmployeeBase):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        return 0
