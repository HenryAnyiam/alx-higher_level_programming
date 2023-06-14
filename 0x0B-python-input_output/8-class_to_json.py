#!/usr/bin/python3

"""8-class_to_json module

func:
    class_to_json

"""


def class_to_json(obj):
    """gets the dictionary description with simple data structure

    Returns:
        Dictionary

    """

    return vars(obj)
