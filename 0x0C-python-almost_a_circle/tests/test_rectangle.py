#!/usr/bin/python3
"""Unittest for rectangle class
"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle

    Args:
        unittest.TestCase: class being inherited from

    """

    def capt(self, method, *args):
        """capture printed output by redirecting it"""

        cap = StringIO()
        sys.stdout = cap
        method(*args)
        text = cap.getvalue()
        sys.stdout = sys.__stdout__
        return text

    def test_instance(self):
        """Test for Rectangle instance"""

        self.assertTrue(Rectangle(1, 2))
        self.assertTrue(Rectangle(1, 2, 3))
        self.assertTrue(Rectangle(1, 2, 3, 4))
        self.assertTrue(Rectangle(1, 2, 3, 4, 5))

    def test_instance_Error(self):
        """Test for correct Error raise"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, "4")

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 2, 3, -4)

    def test_methods(self):
        """Test for various rectangle methods"""

        r1 = Rectangle(4, 6, 2, 1, 2)
        r2 = Rectangle(2, 2)
        r3 = Rectangle(3, 2, 1)
        r4 = Rectangle(3, 2, 1, 1)
        self.assertEqual(r1.area(), 24)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (2) 2/1 - 4/6\n')
        self.assertEqual(self.capt(r2.display), '##\n##\n')
        self.assertEqual(self.capt(r3.display), ' ###\n ###\n')
        self.assertEqual(self.capt(r4.display), '\n ###\n ###\n')
