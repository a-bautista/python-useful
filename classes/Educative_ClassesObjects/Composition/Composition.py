class Engine: 
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)


class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, engine, tires, doors, color):
        '''
            Composition
        '''
        self.engObj = Engine(engine)
        self.tiresObj = Tires(tires)
        self.doorsObj = Doors(doors)
        self.color = color

    def printDetails(self):
        self.engObj.printDetails()
        self.tiresObj.printDetails()
        self.doorsObj.printDetails()
        print("Car color: ", self.color)


car = Car(1600, 4, 2, "White")
car.printDetails()

'''
    In aggregation, the lifetime of the owned object does not depend on the 
    lifetime of the owner.

    This is a Part-Of relationship where One class object must be a part of the other
'''