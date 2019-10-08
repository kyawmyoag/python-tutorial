from employee.base_employee import EmployeeBase
from employee.permanent_employee import PermanentEmployee
from employee.probation_employee import ProbationEmployee

emp_1 = PermanentEmployee('John', 500)
emp_2 = ProbationEmployee('Smith', 100)

print('Permanent Employee - {}, Salary - {}, Bonus - {}'.format(emp_1.name,
                                                                emp_1.salary, emp_1.get_bonus()))

print('Probation Employee - {}, Salary - {}, Bonus - {}'.format(emp_2.name,
                                                               emp_2.salary, emp_2.get_bonus()))
