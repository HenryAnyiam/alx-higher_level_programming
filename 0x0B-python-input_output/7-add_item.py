#!/usr/bin/python3

"""7-add_item module

Reads args, appends to a list and serialize

"""

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = []

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass
else:
    for i in obj:
        items.append(i)
args = sys.argv
if len(args) > 1:
    for i in range(1, len(args)):
        items.append(args[i])
save_to_json_file(items, "add_item.json")
