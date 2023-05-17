#!/usr/bin/python3
def uniq_add(my_list=[]):
    if type(my_list) == list:
        new = list(set(my_list))
        x = 0
        for i in new:
            x += i
        return x
