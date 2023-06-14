#!/usr/bin/python3

"""6-load_from_json_file module

func:
    load_from_json_file

"""

import json


def load_from_json_file(filename):
    """deserializes a json file and return an object

    Args:
        filename: file with json string

    Returns:
        deserialized object

    """

    with open(filename, encoding="UTF-8") as Myfile:
        return json.load(Myfile)
