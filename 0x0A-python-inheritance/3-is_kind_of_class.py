#!/usr/bin/python3

"""3-is_kind_of_class module

func:
    is_kind_of_class

"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a_class

    Args:
        obj: object
        a_class: class to compare obj with

    Returns:
        True if obj is type a_class else false

    """

    if isinstance(obj, a_class):
        return True
    return False
