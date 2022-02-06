class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country name: ", self.name)
        print("Country population: ", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def printDetails(self):
        print("Person Name: ", self.name)
        self.country.printDetails()

c = Country("Canada", 45000)
# aggregation of c in p
p = Person("Jeremy", c)
p.printDetails()


'''
    Aggregation follows the Has-A model. This creates a parent-child 
    relationship between two classes, with one class owning the object 
    of another.

    In aggregation, the lifetime of the owned object does not depend 
    on the lifetime of the owner.

    Aggregation is when objects have their own life cycle and child 
    object can associate with only one owner object.

'''