from math import pi, sqrt

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def getType(self):
        return "shape"

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return pi * self.r * self.r
    
    def perimeter(self):
        return 2 * pi * self.r
    
    def getType(self):
        return "circle"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.w = width
        self.h = height
    
    def area(self):
        return self.w * self.h
    
    def perimeter(self):
        return 2 * self.w + 2 * self.h
    
    def getType(self):
        return "rectangle"

class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    def area(self):
        semiperimeter = self.perimeter() / 2
        return sqrt(
            semiperimeter
            * (semiperimeter - self.l1)
            * (semiperimeter - self.l2)
            * (semiperimeter - self.l3)
        )
    
    def perimeter(self):
        return self.l1 + self.l2 + self.l3
    
    def getType(self):
        return "triangle"

# New Shapes
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def getType(self):
        return "square"

class Ellipse(Shape):
    def __init__(self, semi_major, semi_minor):
        self.a = semi_major
        self.b = semi_minor
    
    def area(self):
        return pi * self.a * self.b
    
    def perimeter(self):
        # Approximation for ellipse perimeter
        return pi * (3 * (self.a + self.b) - sqrt((3 * self.a + self.b) * (self.a + 3 * self.b)))
    
    def getType(self):
        return "ellipse"

# Test Shapes
shapes = [
    Circle(1),
    Rectangle(2, 2),
    Triangle(3, 4, 5),
    Square(4),
    Ellipse(5, 3)
]

for shape in shapes:
    print(
        "shape type:", 
        shape.getType(), 
        "perimeter:", 
        shape.perimeter(), 
        "area:", 
        shape.area(),
    )
