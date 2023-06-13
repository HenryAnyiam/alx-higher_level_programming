#!/usr/bin/python3

"""9-Rectangle module with BaseGeometry class"""


class BaseGeometry:
    """building class"""

    def area(self):
        """raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is int

        Args:
            name: int name
            value: value to be validated

        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """new class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """initialization of class Rectangle

        Args:
            width
            height

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """gets the area of Rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """returnss string representation of class"""

        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
