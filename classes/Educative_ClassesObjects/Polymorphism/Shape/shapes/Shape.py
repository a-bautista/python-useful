from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.sides = 0

    # overridden method
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass
