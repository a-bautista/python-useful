import MyMath as mymath
# from MyMath import add
import unittest
import sys

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    # @unittest.skip('Skip this test')
    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    # @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

class TestSubtract(unittest.TestCase):

    def test_subtract_integers(self):
        """
        Test the subtraction of integer values
        """
        result = mymath.subtract(5, 2)
        self.assertEqual(result, 3)


# if __name__ == '__main__':
#     unittest.main()
# coverage run .\test_mymath.py
# coverage report -m
# coverage html