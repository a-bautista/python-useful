'''
    Operators in Python can be overloaded to operate in a certain user-defined way. 
    Whenever an operator is used in Python, its corresponding method is invoked to 
    perform its predefined function. For example, when the + operator is called, 
    it invokes the special function, __add__, in Python, but this operator acts 
    differently for different data types
'''

class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        # you are calling the main class to do the operations
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp

def main():

    obj1 = Com(3, 7)
    obj2 = Com(2, 5)

    obj3 = obj1 + obj2
    obj4 = obj1 - obj2

    print(obj3.real)
    print(obj3.imag)

    print(obj4.real)
    print(obj4.imag)

main()

'''
Operator	Method
+	__add__ (self, other)
-	__sub__ (self, other)
/	__truediv__ (self, other)
*	__mul__ (self, other)
<	__lt__ (self, other)
>	__gt__ (self, other)
==	__eq__ (self, other)

'''