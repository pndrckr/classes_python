from staff.employee import Employee
from staff.developer import Developer

tom = Employee("Tom", "Andjerry", 5)
bugs = Developer("Bugs", "Bunny", 3, "Python")
daffy = Developer("Daffy", "Duck", 3, "JavaScript")
elmer = Developer("Elmer", "Fudd", 1, "Java")

print Developer.details(elmer)
print Employee.details(tom)
print (bugs.details())
print (Developer.details(daffy))
