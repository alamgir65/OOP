from math import pi
class Shape:
    def __init__(self,name) -> None:
        self.name = name
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, name,length,width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius = radius
        super().__init__(name)
    def area(self):
        return pi * (self.radius ** 2)
    
class Triangle(Shape):
    def __init__(self, name,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
        super().__init__(name)
    def area(self):
        return self.a * self.b * self.c
    
    
circle = Circle('Circle',3)
print(circle.area())

rectangle = Rectangle('Rectangle',23,4)
print(rectangle.area())

triangle = Triangle('Triangle',2,3,4)
print(triangle.area())