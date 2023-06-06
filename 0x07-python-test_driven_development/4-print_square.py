#!/usr/bin/python3

"""4-print_square module

functions:
    print_square

"""


def print_square(size):
    """ prints # in square to stdout

    Args:
        size: size of square

    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(size):
            print("#" * size)
