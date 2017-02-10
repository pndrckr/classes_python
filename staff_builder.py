from staff.employee import Employee
from staff.developer import Developer

tom = Employee("Tom", "Andjerry", 5, 456)
bugs = Developer("Bugs", "Bunny", 3, 457, "Python")
daffy = Developer("Daffy", "Duck", 3, 845, "JavaScript")
elmer = Developer("Elmer", "Fudd", 1, 840, "Phyton")

print Employee.details(tom)
print (bugs.details())
print (Developer.details(daffy))
print Developer.details(elmer)