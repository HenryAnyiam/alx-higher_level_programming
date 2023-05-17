#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if type(a_dictionary) == dict:
        new = {}
        for i in a_dictionary.keys():
            new[i] = a_dictionary[i] * 2
        return new
    return None
