class Animal:
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def speak(self):
        print("Woof! I am a dog.")

dog = Dog()
dog.speak()