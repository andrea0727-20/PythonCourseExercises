import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 
    

circle = Circle(5)
print("Área del círculo:", circle.area())

square = Square(4)
print("Área del cuadrado:", square.area()) 