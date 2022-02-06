from math import pow
class Point:
    
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        # return (pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        return ((self.x **2)+ (self.y **2) + (self.z **2))
        