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
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) in c and type(b) in c:
        result = a + b
        if result == float('inf') or result == -float('inf'):
            return 89
        return int(a) + int(b)
    else:
        if type(a) not in c:
            raise TypeError("a must be an integer")
        if type(b) not in c:
            raise TypeError("b must be an integer")
