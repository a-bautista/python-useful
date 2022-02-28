from unittest.mock import create_autospec
def add(a, b):
    return a + b

mocked_func = create_autospec(add, return_value='Right amount of values')
print (mocked_func(1, 2))
# Right amount of values

mocked_func(1, 2, 3)