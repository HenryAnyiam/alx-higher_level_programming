#!/usr/bin/python3

"""2-is_same_class module

func:
    is_same_class

"""
def is_same_class(obj, a_class):
    """checks if obj is of type a_class

    Args:
        obj: object
        a_class: class to compare obj with

    Returns:
        True if obj is type a_class else false

    """

    if type(obj) is a_class:
        return True
    return False
