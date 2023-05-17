#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        new = list(a_dictionary.items())
        for i in new:
            if i[1] == value:
                del a_dictionary[i[0]]
    return a_dictionary
