class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Leo", 7)
dog2 = Dog("Tiger", 9)
dog3 = Dog("jehangir", 3)

def get_biggest_number(*args):
    return max(args)

print("maximum age among the dog is: ",get_biggest_number(dog1.age, dog2.age, dog3.age))