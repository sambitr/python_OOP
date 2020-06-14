class Person():
    totalPerson = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.totalPerson += 1

    def displayDetails(self):
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, id_no, salary):
        self.id_no = id_no
        self.salary = salary
        Person.__init__(self, name, age) ##Initiating the parent class to make the parent class instance attributes available to child class


emp1 = Employee("sachin", 32, 1010101, 320000 )
emp1.displayDetails()
print("Total persons: ", emp1.totalPerson)