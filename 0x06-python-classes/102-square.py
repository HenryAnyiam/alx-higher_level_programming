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

    def __lt__(self, other):
        """answer to less than

        Returns:
            True if less than other
        """

        return self.__size < other.__size

    def __gt__(self, other):
        """answer to greater than

        Returns:
            True if greater than
        """

        return self.__size > other.__size

    def __eq__(self, other):
        """answer to equals to

        Returns:
            True if equivalent to
        """

        return self.__size == other.__size

    def __ne__(self, other):
        """answer to not equals to

        Returns:
            True if not equals to
        """
        return self.__size != other.__size

    def __ge__(self, other):
        """answers to greater than or equals to

        Returns:
            True if greater than or equals to
        """

        return self.__size >= other.__size
    
    def __le__(self, other):
        """answers to less than or equals to

        Returns:
            True if less than or equals to
        """

        return self.__size <= other.__size

    @property
    def size(self):
        """gets private attribute size

        setter checks if size is int and greater than or
        equals to 0

        """

        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) or isinstance(size, float):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
