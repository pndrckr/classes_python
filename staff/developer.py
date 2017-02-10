from employee import Employee

class Developer(Employee):
    def __init__(self, fname, sname, no_of_years, employee_number, prog_lenguage):
        self.prog_lenguage = prog_lenguage
        Employee.__init__(self, fname, sname, no_of_years, employee_number)

    def calculate_salary(self):
        bonus = 0
        standard = Employee.calculate_salary(self)
        if self.prog_lenguage.lower() == 'python':
            bonus = standard * .10
        return standard + bonus

    def details(self):
        return Employee.details(self) + ' Programing Language: %s\n' % self.prog_lenguage
