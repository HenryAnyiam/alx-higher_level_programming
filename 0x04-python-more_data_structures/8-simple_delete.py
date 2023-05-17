#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if type(a_dictionary) == dict:
        if key in a_dictionary.keys():
            del a_dictionary[key]
    return a_dictionary
