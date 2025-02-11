class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width  

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
rectangle1 = Rectangle(5, 3)

print("Área:", rectangle1.area())
print("Perímetro:", rectangle1.perimeter())