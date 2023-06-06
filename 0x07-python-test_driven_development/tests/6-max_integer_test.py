#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test class for the function maxinteger

    Args:
        unittest.TestCase: class being inherited from

    """

    def test_integer(self):
        """Tests with positive integers"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5]), 5)

    def test_negative(self):
        """Tests with negative integers"""

        self.assertEqual(max_integer([-10, -8, -15, -8]), -8)
        self.assertEqual(max_integer([-12, 12, 0, -20]), 12)
        self.assertEqual(max_integer([-12, -26, 0, 0]), 0)

    def test_len_data(self):
        """Tests with other data structures that has len attribute"""

        self.assertEqual(max_integer("Hello"), 'o')
        self.assertEqual(max_integer("HellO"), 'l')
        self.assertEqual(max_integer("14325"), '5')
        self.assertEqual(max_integer({1:8, 2:4, 0:10}), 10)

    def test_error(self):
        """Tests with possible error cases"""

        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 1543)
        self.assertRaises(KeyError, max_integer, {1:8, 4:4, 0:10})

    def test_empty(self):
        """Tests with empty lists"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
