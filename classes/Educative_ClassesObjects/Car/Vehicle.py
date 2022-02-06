class Vehicle:
    
    mpg = 40

    def __init__(self, make, color, year) -> None:
        self.make = make
        self.color = color
        self.year = year

    def printDetails(self) -> None:
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Year:", self.year)
