#!/usr/bin/python3

"""3-to_json_string module

func:
    to_json_string

"""

import json


def to_json_string(my_obj):
    """converts an object to string

    Args:
        my_obj: object to serialize

    Returns:
        JSON string

    """

    return json.dumps(my_obj)
