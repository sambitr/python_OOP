##Parent class
class Dog():

    type = "mammals" #class attribute

    def __init__(self, name, age): ##instance attributes
        self.name = name
        self.age = age

    def description(self):
        return("{} is {} years old".format(self.name, self.age))
    def speak(self, sound):
        return("{} speaks {}".format(self.name, sound))

##child class inherits from parent class
class Husky(Dog):
    def run(self, speed):
        return("{} runs at {} speed".format(self.name, speed))

##child class inherits from parent class
class Labrador(Dog):
    def run(self, speed):
        return("{} runs at {}".format(self.name, speed))

jim = Husky("jim", 12)
print(jim.description())
print(jim.speak("Gruff Gruff"))
print(jim.run(12))
