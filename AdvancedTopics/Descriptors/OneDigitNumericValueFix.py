class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumericValue("number")

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)