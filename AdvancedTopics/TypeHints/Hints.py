# overloading a method with singledispatch

from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported Type')

@add.register(int)
def _(a: int, b: int) -> int:
    print("First argument is of type: ", type(a))
    print(a + b)
    return a + b

@add.register(str)
def _(a: str, b: str) -> str:
    print("First argument is of type: ", type(a))
    print(a + b)
    return a + b


def main():
    add(5, 5)

main()
