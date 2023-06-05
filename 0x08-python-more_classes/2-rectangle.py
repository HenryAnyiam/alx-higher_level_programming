#!/usr/bin/python3
"""2-rectangle module for class Rectangle"""


class Rectangle:
    """Represents a Rectangle class """

    def __init__(self, width=0, height=0):
        """instantiation of class Rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets private attribute width

        setter ensures width is greater than
        or equal to 0

        """

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and value >= 0:
            self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """gets private attribute height

        setter ensures height is greater than or
        equal to 0

        """

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and value >= 0:
            self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """gets the area of a rectangle

        Returns:
            area of the rectangle

        """

        return self.__width * self.__height

    def perimeter(self):
        """gets the perimeter of a rectangle

        Returns:
            perimeter of the rectangle

        """

        if self.__width != 0 and self.__height != 0:
            return ((self.__width + self.__height) * 2)
        return 0
