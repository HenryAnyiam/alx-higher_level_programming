#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) == dict:
        if len(a_dictionary) == 0:
            return None
        a = list(a_dictionary.items())
        a.sort(key=lambda n: n[1])
        return a[-1][0]
    return None
