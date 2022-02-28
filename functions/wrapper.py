# from functools import wraps
def another_function(func):
    """
        A function that accepts another function
    """
    # @wraps(func)
    def wrapper():
        """
            A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper

@another_function
def a_function():
    """
        A pretty useless function
    """
    return 1+1

if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)

"""
    another_function() is a wrapper for a_function() and it changes the properties
    of a_function().
    Finally we looked at wraps which had a very narrow focus: namely 
    it fixes docstrings and function names that have been decorated 
    such that they don’t have the decorator’s docstring or name any more.
    wraps fixes the problem of docstring and names.

"""