def get_user_input():
    """
        No parameters in this function.

        Prompt the user an integer value for your function. 

        If the value is not an integer, then continue the prompt.

        Return the integer value given by the user.

        Call this docstring with print(get_user_input.__doc__)
    """

    value = input("Enter a numeric value for your function: \n")

    if isinstance(value, str):
        while not value.isnumeric():
            value = input("Enter a numeric value for your function: \n")
    print("You entered a numeric value: "+ str(value))


def greeter(name, title='Dr', prompt='Welcome', message='Live long'):
    '''
        Named function
    '''
    print(prompt, title, name, message)


def my_function(*args, **kwargs):
    '''
        Positional and keyword arguments
    '''
    for arg in args:
        print('arg:', arg)

    for key in kwargs.keys():
        print('key:', key, 'value:', kwargs[key])


def outer():
    title = 'original title'

    def inner():
        nonlocal title
        title = 'title changed'
        print('inner: ', title)
    inner()
    print('outer: ', title)


# pre to decorators (higher level functions)
def make_function():
    def adder(x, y):
        return x + y
    return adder

# pre to decorators (higher level functions)
def make_checker(num):
    '''
        Return a boolean value based on the input value
    '''
    if num == 'even':
        return lambda n: n%2 == 0
    elif num == 'positive':
        return lambda n: n >= 0
    else: 
        raise ValueError('Unknown request')

# curried function or binding
def multiply(a, b):
    return a * b

def multby(func, num):
    return lambda y: func(num, y)

def main():
    # print("Starting")
    
    # get_user_input() # 0 arguments in the function

    # print("End")

    # named arguments
    greeter('Alex', message='Happy coding!', title='Sr')

    # print(get_user_input.__doc__)

    # positional and keyword arguments
    my_function('Susan','Jennifer', 'Sharon', name='Oscar', age=23, profession='Student')

    func0 = lambda i: i*i
    print(func0(4))

    # non-local 
    outer()

    # pre to decorators
    f1 = make_function()
    print(f1(3,5))

    f2 = make_checker('even')
    print(f2(2))

    # fix the function with the number 2
    double = multby(multiply,2)

    # invoke the curried function
    print(double(5))


main()