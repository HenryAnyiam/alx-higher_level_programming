#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if type(my_list) == list:
        return [x if x != search else replace for x in my_list]
