#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) == dict:
        for i in sorted(a_dictionary):
            print(f"{i}: {a_dictionary[i]}")
