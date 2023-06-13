#!/usr/bin/python3

"""7-base_geometry module with BaseGeometry class"""


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
