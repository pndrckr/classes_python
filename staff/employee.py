class Employee(object):
    BASE_SALARY = 5000

    def __init__(self, fname, sname, no_of_years, employee_number):
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        self.employee_number = employee_number

    #  calculate the ase salary plus any bonus based on the number of years worked

    def calculate_salary(self):
        bonus = 5000
        salary = self.BASE_SALARY
        if self.no_of_years < 3:
                bonus = salary * 0.01
        elif self.no_of_years <= 5:
                bonus = salary * 0.05
        elif self.no_of_years > 5:
                bonus = salary * 0.25
        return salary * bonus

    def details(self):
        return "First Name: %s\n Surname: %s\n Years Worked: %s\n Employee Number: %s\n Salary: %s\n" % (
            self.fname, self.sname, self.no_of_years, self.employee_number, self.calculate_salary())



tom = Employee ("Tom", "Birdy", 5, 456)


print Employee.details(tom)