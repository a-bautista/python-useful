class Car:
    def __init__(self, brand, color):
        self.color   = color
        self.brand = brand
    
    def __repr__(self):
        '''This is unambiguous and this appears in the terminal.'''
        return f'{self.__class__.__name__}('f'{self.brand}, {self.color})'
        
        
    def __str__(self):
        '''This is for the customer.'''
        return f'This is a {self.color} car and brand {self.brand}'


