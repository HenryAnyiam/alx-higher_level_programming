#!/usr/bin/python3

"""4-from_json_string module

func:
    from_json_string

"""


import json


def from_json_string(my_str):
    """deserializes a string to its equivalent object

    Args:
        my_str: JSON string

    Return:
        Object

    """

    return json.loads(my_str)
