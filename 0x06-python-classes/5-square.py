#!/usr/bin/python3
"""2-square.py Second module, extension of class Square"""


class Square:
    """class Square, further building"""

    def __init__(self, size=0):
        """initialization of class Square
        Args:
            size: size of square

        """
        self.size = size

    @property
    def size(self):
        """gets private attribute size

        setter checks if size is int and greater than or
        equals to 0

        """

        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """gets the area of the square

        Returns:
            area of the square

        """

        return self.__size ** 2

    def my_print(self):
        """prints to stdout the square with #"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
