#!/usr/bin/python3

"""100-append_after module

func:
    append_after

"""


def append_after(filename="", search_string="", new_string=""):
    """reads throgh a file and adds new string

    Args:
        filename: name of file
        search_string: string to search
        new_string: new string to add

    """

    with open(filename, "r", encoding="UTF-8") as MyFile:
        hold = ""
        for line in MyFile:
            hold += line
            if search_string in line:
                hold += new_string
    with open(filename, "w", encoding="UTF-8") as MyFile:
        MyFile.write(hold)
