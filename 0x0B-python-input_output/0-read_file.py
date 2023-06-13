#!/usr/bin/python3

"""0-read_file module

func:
    read_file

"""


def read_file(filename=""):
    """read from a file and writes to stdout

    Args:
        filename - name of file

    """

    with open(filename, encoding="UTF-8") as MyFile:
        print(MyFile.read(), end="")
