#!/usr/bin/python3
"""Build class to match python bytecode"""

import math


class MagicClass:
    """class MagicClass to match bytecode"""

    def __init__(self, radius=0):
        """initialize MagicClass"""

        self.__radius = radius

    @property
    def radius(self):
        """gets private attribute radius

        setter checks if radius is int or float

        """

        return self.__radius

    @radius.setter
    def radius(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """calculates the area of the class

        Returns:
            area
        """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculates the circumference of the class

        Returns:
            circumference
        """

        return 2 * math.pi * self.__radius
