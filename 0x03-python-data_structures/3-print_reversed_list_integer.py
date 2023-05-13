#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lent = len(my_list) - 1
    for i in range(lent, -1, -1):
        print("{:d}".format(my_list[i]))
