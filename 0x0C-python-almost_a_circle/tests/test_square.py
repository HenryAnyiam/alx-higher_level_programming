#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
import sys
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for class Square

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
        """Test for Square instance"""

        self.assertTrue(Square(1, 2))
        self.assertTrue(Square(1, 2, 3))
        self.assertTrue(Square(1, 2, 3, 4))

    def test_instance_Error(self):
        """Test for correct Error raise"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square("1", 2)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, "3")

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-1, 2)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(1, 2, -3)

    def test_methods(self):
        """Test for various Square methods

        Methods:
            area()
            display()
            __str__
            to_dictionary()
            update()

        """

        r1 = Square(4, 2, 1, 2)
        r2 = Square(2)
        r3 = Square(2, 2)
        r4 = Square(2, 2, 1)
        dic = {'x': 2, 'y': 1, 'id': 2, 'size': 4}
        self.assertEqual(r1.area(), 16)
        self.assertEqual(self.capt(print, r1), '[Square] (2) 2/1 - 4\n')
        self.assertEqual(self.capt(r2.display), '##\n##\n')
        self.assertEqual(self.capt(r3.display), '  ##\n  ##\n')
        self.assertEqual(self.capt(r4.display), '\n  ##\n  ##\n')
        self.assertEqual(r1.to_dictionary(), dic)
        r1.update()
        self.assertEqual(self.capt(print, r1), '[Square] (2) 2/1 - 4\n')
        r1.update(89)
        self.assertEqual(self.capt(print, r1), '[Square] (89) 2/1 - 4\n')
        r1.update(89, 1)
        self.assertEqual(self.capt(print, r1), '[Square] (89) 2/1 - 1\n')
        r1.update(89, 1, 2)
        self.assertEqual(self.capt(print, r1), '[Square] (89) 2/1 - 1\n')
        r1.update(89, 1, 2, 3)
        self.assertEqual(self.capt(print, r1), '[Square] (89) 2/3 - 1\n')
        r2.update(**{'id': 89})
        self.assertEqual(self.capt(print, r2), '[Square] (89) 0/0 - 2\n')
        r2.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.capt(print, r2), '[Square] (89) 0/0 - 1\n')
        r2.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.capt(print, r2), '[Square] (89) 0/0 - 1\n')
        r2.update(**{'id': 89, 'size': 1, 'x': 3})
        self.assertEqual(self.capt(print, r2), '[Square] (89) 3/0 - 1\n')
        r2.update(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(self.capt(print, r2), '[Square] (89) 3/4 - 1\n')

    def test_more_methods(self):
        """Tests more Square methods"""

        r1 = Square.create(**{'id': 89})
        r2 = Square.create(**{'id': 89, 'size': 1})
        r3 = Square.create(**{'id': 89, 'size': 1, 'x': 3})
        dic = {'id': 89, 'size': 1, 'x': 3, 'y': 4}
        r4 = Square.create(**dic)
        self.assertEqual(self.capt(print, r1), '[Square] (89) 0/0 - 3\n')
        self.assertEqual(self.capt(print, r2), '[Square] (89) 0/0 - 1\n')
        self.assertEqual(self.capt(print, r3), '[Square] (89) 3/0 - 1\n')
        self.assertEqual(self.capt(print, r4), '[Square] (89) 3/4 - 1\n')
        Square.save_to_file(None)
        with open("Square.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), '[]\n')
        Square.save_to_file([])
        with open("Square.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), '[]\n')
        Square.save_to_file([Square(1)])
        dic = '[{"id": 25, "size": 1, "x": 0, "y": 0}]\n'
        with open("Square.json", encoding="UTF-8") as MyFile:
            self.assertEqual(self.capt(print, MyFile.read()), dic)
        L2 = Square.load_from_file()
        dic = '[Square] (25) 0/0 - 1\n'
        self.assertEqual(self.capt(print, L2[0]), dic)
