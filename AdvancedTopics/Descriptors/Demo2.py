class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("access to the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError('Cannot change the value')

class Foo():
    attribute1 = Verbose_attribute()

def main():
    test = Foo()
    # we get access to the attribute1, so we return 42
    x = test.attribute1
    print(x)

main()
