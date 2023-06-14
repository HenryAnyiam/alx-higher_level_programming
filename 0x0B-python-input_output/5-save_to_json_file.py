#!/usr/bin/python3

"""5-save_to_json_file module

func:
    save_to_json_file

"""

import json


def save_to_json_file(my_obj, filename):
    """serialize an object and save to a file

    Args:
        my_obj: object to serialize
        filename: name of file to save to

    """

    with open(filename, "w", encoding="UTF-8") as MyFile:
        json.dump(my_obj, MyFile)
