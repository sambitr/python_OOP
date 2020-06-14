class Parent():
    def __init__(self, name):
        self.name = name

    def getdetails(self):
        print(self.name)

class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)
        self.age = age

    def getAge(self):
        print(self.age)

class GranndChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(name, age)
        self.address = address

    def getAddress(self):
        print(self.address)

GC = GranndChild("sambit", 30, "Bhubaneswar")
GC.getdetails()
GC.getAge()
GC.getAddress()