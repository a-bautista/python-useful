import unittest

from test_mymath import TestAdd

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestAdd))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

'''
    The Test Suite allows you to be more in control of the flow
    of the tests instead of using the unittest.main()

    python .\TestSuite.py
    
'''