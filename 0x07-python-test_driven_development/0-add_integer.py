#!/usr/bin/python3

""" module with function to add integer

    add_integer:
        add two integer
"""


def add_integer(a, b=98):
    """Returns:
        addition or raise error
    """

    c = [int, float]
    if type(a) in c and type(b) in c:
        return int(a) + int(b)
    else:
        if type(a) not in c:
            raise TypeError("a must be an integer")
        if type(b) not in c:
            raise TypeError("b must be an integer")
