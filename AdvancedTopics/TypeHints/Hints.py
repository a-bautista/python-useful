# overloading a method with singledispatch

from functools import singledispatch
from decimal import Decimal

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

@add.register(float)
@add.register(Decimal)
def _(a: float, b:float) -> float:
    print("First argument is of type: ", type(a))
    print(a + b)
    return a + b

def main():
    add(Decimal(5), Decimal(5))
    add(5.0, 5.0)

main()
