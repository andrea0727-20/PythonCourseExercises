class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Johanna", 29)

person1.introduce() 