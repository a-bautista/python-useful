from shapes.Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.sides = 4 # inherited from the Shapes class

    # overriding method
    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return self.sides * self.length

