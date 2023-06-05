#!/usr/bin/python3
"""5-rectangle module for class Rectangle"""


class Rectangle:
    """Represents a Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation of class Rectangle"""

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """prints a messange once an object
        is deleted"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def __str__(self):
        """creates string representation of Rectangle
        object with character #

        Returns:
            square string

        """

        result = ""
        rep = str(self.print_symbol)
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                result += (rep * self.__width)
                if i != (self.__height - 1):
                    result += '\n'
            return result
        return result

    def __repr__(self):
        """creates object representation of
        current rectangle

        Returns:
            object representation of current instance

        """

        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two instance of Rectangle

        Returns:
            the bigger instance or rect_1 if equal

        """

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        res1 = rect_1.area()
        res2 = rect_2.area()
        if res2 == res1:
            return rect_1
        if res2 > res1:
            return rect_2
        return rect_1
