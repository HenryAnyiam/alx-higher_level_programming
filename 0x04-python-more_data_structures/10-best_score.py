#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        a = list(a_dictionary.items())
        a.sort(key=lambda n: n[1])
        return a[-1][0]
    return None
