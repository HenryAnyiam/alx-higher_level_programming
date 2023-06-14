#!/usr/bin/python3

"""1-write_file module

funcs:
    write_file

"""


def write_file(filename="", text=""):
    """writes to a file

    Args:
        filename: name of file
        text: text to write to file

    Returns:
        number of text written to file

    """

    num = 0
    with open(filename, 'w', encoding="UTF-8") as MyFile:
        num = MyFile.write(text)
    return num
