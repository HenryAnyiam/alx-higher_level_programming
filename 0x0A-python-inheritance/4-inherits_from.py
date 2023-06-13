#!/usr/bin/python3

"""4-inherits_from.py module

func:
    inherits_from

"""


def inherits_from(obj, a_class):
    """checks if obj inherits from a_class

    Args:
        obj: object
        a_class: class to compare obj with

    Returns:
        True if obj inherits from a_class else false

    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
