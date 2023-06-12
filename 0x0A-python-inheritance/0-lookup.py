#!/usr/bin/python3
"""0-lookup module

func:
    lookup

"""


def lookup(obj):
    """returns a list of method and attribute
    in an object

    Args:
        obj

    Returns:
        list of methods and attributes

    """

    if type(obj) == type:
        return dir(obj)
