class Foo():
    @property
    def attribute1(self) -> object:
        print("access to the attribute to get the value")
        return 42
    
    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

def main():
    test = Foo()
    x = test.attribute1
    print(x)
    print(test.__dict__)

main()


'''
    Descriptors are Python objects that implement a method of the descriptor 
    protocol, which gives you the **ability to create objects that have special 
    behavior when they’re accessed as attributes of other objects.**

    __get__(self, obj, type=None) -> object
    __set__(self, obj, value) -> None
    __delete__(self, obj) -> None
    __set_name__(self, owner, name)

    If your descriptor implements just .__get__(), then it’s said to be a 
    non-data descriptor. If it implements .__set__() or .__delete__(), 
    then it’s said to be a data descriptor.

     In Python, every object has a built-in __dict__ attribute. 
     This is a dictionary that contains all the attributes defined in the 
     object itself. 

'''