class EmployeeBase:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_employee_name(self):
        return self.name
    
    def get_employee_salary(self):
        return self.salary