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
    def size(self, size):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
