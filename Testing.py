
assert sum([1, 2, 3]) == 6, "Should be 6"
>> 



# Defining a test function
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

# Manually calling the test function
test_sum()

# If no error shows up, the test passed
print("Everything passed")

>> Everything passed


Writing Your First Test

# This code contains a test that will fail
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"  # This will raise an error because 1+2+2 = 5

# Run the tests
test_sum()
test_sum_tuple()  # This line causes an AssertionError

print("Everything passed")

>> test_sum() passed
>> test_sum_tuple() failed



  
# my_sum/__init__.py

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

>> 





# test.py

import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

>> 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


my_sum/__init__.py:


def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total



 test.py:

import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)  # This test is expected to fail

if __name__ == '__main__':
    unittest.main()

