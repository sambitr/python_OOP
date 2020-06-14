class Dog():

    type = "mammals" #class attribute

    def __init__(self, name, age): ##instance attributes
        self.name = name
        self.age = age
        ##or you can declare by using below as well:
        ##Dog.name = name
        ##Dog.age = age

    ##instance methods.
    ##They have a mandatory single argument: self
    def description(self):
        return("{} is {} years old".format(self.name, self.age))
    def speak(self, sound):
        return("{} speaks {}".format(self.name, sound))


dog1 = Dog("Leo", 3)   ##creating instances of the class
print(dog1.description())
print(dog1.speak("gruff gruff"))

