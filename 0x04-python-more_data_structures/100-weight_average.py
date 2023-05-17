#!/usr/bin/python3
def weight_average(my_list=[]):
    if type(my_list) == list:
        if len(my_list) == 0:
            return 0
        total = 0
        weight = 0
        for i in my_list:
            if type(i) != tuple:
                return 0
            if type(i[0]) != int != type(i[1]):
                return 0
            if len(i) != 2:
                return 0
            total += i[0] * i[1]
            weight += i[1]
        return total / weight
