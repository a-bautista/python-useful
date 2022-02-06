class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        # return self.__length * self.__width
        # a = self.getLength()
        # b = self.getWidth()
        # return a * b
        return self.getLength()* self.getWidth()

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width