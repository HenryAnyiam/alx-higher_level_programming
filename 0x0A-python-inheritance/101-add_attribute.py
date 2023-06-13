#!/usr/bin/python3

"""101-add_attribute module

func:
    add_attribute

"""


def add_attribute(obj, attr, value):
    """checks if a class allows for new attribute
    and add new attribute if it does

    Args:
        obj: object
        attr: new attribute
        value: value to new attribute

    """

    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
