'''
    What is the difference between is and ==?
    
    The “==” operator compares the value or equality of two objects, 
    whereas the Python “is” operator checks whether two variables point 
    to the same object in memory.

    What is the difference between is and == and __eq__?

'''
class StudentImproved:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, StudentImproved):
            if other.name == self.name:
                return True
        return False

class Student:
    def __init__(self, name):
        self.name = name
  
  
alex = Student("alex")
jesus = Student("jesus")

ivan = StudentImproved("ivan")
ivan2 = StudentImproved("ivan")
  
print("alex == jesus : ", (alex == jesus))
print("ivan == ivan2 : ", (ivan == ivan2))

x = [1, 2]
y = [1, 2]
z = y
print("x is y : ", x is y)
print("z is y : ", z is y)



'''
    When you instantiate this class and try to compare these 2 objects
    then Python won't know how to compare them, you need to define that with
    the __eq__
'''

