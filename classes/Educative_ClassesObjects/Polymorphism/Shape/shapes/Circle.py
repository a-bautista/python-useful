from shapes.Shape import Shape
from math import pi

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    # overriding method
    def getArea(self):
        return pi * self.radius**2

    def getPerimeter(self):
        return 2 * pi * self.radius ** 2