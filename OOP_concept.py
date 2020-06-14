class Dog():

    type = "mammals" #class attribute

    def __init__(self, name, age): ##instance attributes
        self.name = name
        self.age = age
        ##or you can declare by using below as well:
        ##Dog.name = name
        ##Dog.age = age

dog1 = Dog("Leo", 3)   ##creating instances of the class
dog2 = Dog("Tiger", 4)

if dog1.type == "mammals":
    print(dog1.name, dog1.age)
else:
    print("not a choise")