#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        high = list(a_dictionary.keys())[0]
        highest = a_dictionary[high]
        for i in a_dictionary:
            if a_dictionary[i] > highest:
                highest = a_dictionary[i]
                high = i
        return high
    return None
