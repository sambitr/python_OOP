class Employee():

    empCount = 0

    def __init__(self, name, emp_no):
        self.name = name
        self.emp_no = emp_no
        Employee.empCount += 1 ##Class vairiable should be accessed only by the Class name

    def displayCount(self):
        return("Total number of employyes are:{}".format(self.empCount))
    def displayEmployeeDetails(self):
        return("{} employee number belongs to {}".format(self.emp_no, self.name))

emp1 = Employee("Sam", 100)
emp2 = Employee("Sachin", 101)

print(emp1.displayCount())

print(emp1.displayEmployeeDetails())
print(emp2.displayEmployeeDetails())

##modifying the class attribute
emp1.name = "Rahul"
print(emp1.displayEmployeeDetails())

##Built-In Class Attributes
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

