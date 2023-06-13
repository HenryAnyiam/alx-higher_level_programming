#!/usr/bin/python3

"""100-my_int module with class inheriting from int"""


class MyInt(int):
    """inherits from class int"""

    def __eq__(self, other):
        """reverses the __eq__ method of int

        Args:
            other: other class

        """

        return self.numerator != other.numerator

    def __ne__(self, other):
        """reverses the __ne__ method of int

        Args:
            other: other class to compare

        """

        return self.numerator == other.numerator
