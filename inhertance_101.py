class Dog():

    type = "mammals" #class attribute

    def __init__(self, name, age): ##instance attributes
        self.name = name
        self.age = age

    def description(self):
        return("{} is {} years old".format(self.name, self.age))
    def speak(self, sound):
        return("{} speaks {}".format(self.name, sound))

class Husky(Dog):
    def run(self, speed):
        return("{} runs at {} speed".format(self.name, speed))

class Labrador(Dog):
    def run(self, speed):
        return("{} runs at {} speed".format(self.name, speed))

jim = Husky("jim", 12)
print(jim.description())
print(jim.speak("Gruff Gruff"))
print(jim.run(12))
