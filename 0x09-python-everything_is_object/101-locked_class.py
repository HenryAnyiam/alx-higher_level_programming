#!/usr/bin/python3
"""101-locked_class module"""


class LockedClass:
    """defines a class that allows only
    one attribute
    """

    __slots__ = ("first_name",)
