#!/usr/bin/python3
"""2-square.py Second module, extension of class Square"""


class Square:
    """class Square, further building"""

    def __init__(self, size=0, position=(0, 0)):
        """initialization of class Square

        Args:
            size: size of square
            position: tuple with coordinates of square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets private attribute position

        setter checks that position is a tuple
        of two positive integers

        """

        return self.__position

    @position.setter
    def position(self, value):
        error = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(error)
        else:
            raise TypeError(error)

    def area(self):
        """gets the area of the square

        Returns:
            area of the square

        """

        return self.__size ** 2

    def my_print(self):
        """prints to stdout the square with #"""


        print("\n" * self.position[1], end='')
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            for j in range(self.__size):
                print("#", end='')
            print()
