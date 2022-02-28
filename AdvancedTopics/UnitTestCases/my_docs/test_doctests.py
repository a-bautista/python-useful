import doctest
import my_docs
# import unittest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_docs))
    return tests

'''
    Run your test cases from the docs defined in each function with the 
    command python -m unittest discover
'''