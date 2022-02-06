from Vehicle import Vehicle

class Car(Vehicle):
    
    mpg = 30

    def __init__(self, make, color, year, model):
        # call the constructor from the parent class
        # Vehicle.__init__(self, make, color, year)
        super().__init__(make, color, year)
        self.model = model
    

    def printCarDetails(self):
        # call the parent class 
        # self.printDetails()
        super().printDetails()
        print("Model:", self.model)

    def displayMPG(self):
        print("Display the Vehicle (parent) MPG: "+str(super().mpg))
        print("Display the Car MPG: "+str(self.mpg))

    def __repr__(self):
        '''This is unambiguous and this appears in the terminal.'''
        return f'{self.__class__.__name__}('f'{self.brand}, {self.color})'
        
        
    def __str__(self):
        '''This is for the customer.'''
        return f'This is a {self.color} car and brand {self.brand}'


