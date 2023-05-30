#!/usr/bin/python3
"""2-square.py Second module, extension of class Square"""


class Square:
    """class Square, further building"""

    def __init__(self, size=0):
        """initialization of class Square
        Args:
            size: size of square

        """
        self.set_size(size)

    def set_size(self, size):
        """set private attribute

        Args:
            size: size of Square

        """

        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def get_size(self):
        """gets private attribute size

        Returns:
            size of square

        """

        return self.__size
