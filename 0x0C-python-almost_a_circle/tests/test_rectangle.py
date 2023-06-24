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
        """Test for various rectangle methods

        Methods:
            area()
            display()
            __str__
            to_dictionary()
            update()

        """

        r1 = Rectangle(4, 6, 2, 1, 2)
        r2 = Rectangle(2, 2)
        r3 = Rectangle(3, 2, 1)
        r4 = Rectangle(3, 2, 1, 1)
        dic = {'x': 2, 'y': 1, 'id': 2, 'height': 6, 'width': 4}
        self.assertEqual(r1.area(), 24)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (2) 2/1 - 4/6\n')
        self.assertEqual(self.capt(r2.display), '##\n##\n')
        self.assertEqual(self.capt(r3.display), ' ###\n ###\n')
        self.assertEqual(self.capt(r4.display), '\n ###\n ###\n')
        self.assertEqual(r1.to_dictionary(), dic)
        r1.update()
        self.assertEqual(self.capt(print, r1), '[Rectangle] (2) 2/1 - 4/6\n')
        r1.update(89)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 2/1 - 4/6\n')
        r1.update(89, 1)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 2/1 - 1/6\n')
        r1.update(89, 1, 2)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 2/1 - 1/2\n')
        r1.update(89, 1, 2, 3)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 3/1 - 1/2\n')
        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 3/4 - 1/2\n')
        r2.update(**{'id': 89})
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 0/0 - 2/2\n')
        r2.update(**{'id': 89, 'width': 1})
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 0/0 - 1/2\n')
        r2.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 0/0 - 1/2\n')
        r2.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 3/0 - 1/2\n')
        r2.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 3/4 - 1/2\n')

    def test_more_methods(self):
        """Tests more Rectangle methods"""

        r1 = Rectangle.create(**{'id': 89})
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        dic = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r5 = Rectangle.create(**dic)
        self.assertEqual(self.capt(print, r1), '[Rectangle] (89) 0/0 - 3/1\n')
        self.assertEqual(self.capt(print, r2), '[Rectangle] (89) 0/0 - 1/1\n')
        self.assertEqual(self.capt(print, r3), '[Rectangle] (89) 0/0 - 1/2\n')
        self.assertEqual(self.capt(print, r4), '[Rectangle] (89) 3/0 - 1/2\n')
        self.assertEqual(self.capt(print, r5), '[Rectangle] (89) 3/4 - 1/2\n')
        L1 = Rectangle.load_from_file()
        self.assertEqual(self.capt(print, L1), '[]\n')
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), '[]\n')
        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), '[]\n')
        Rectangle.save_to_file([Rectangle(1, 2)])
        dic = '[{"id": 14, "width": 1, "height": 2, "x": 0, "y": 0}]\n'
        with open("Rectangle.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), dic)
        L2 = Rectangle.load_from_file()
        dic = '[Rectangle] (14) 0/0 - 1/2\n'
        self.assertEqual(self.capt(print, L2[0]), dic)
