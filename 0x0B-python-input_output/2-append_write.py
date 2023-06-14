#!/usr/bin/python3

"""2-append_write module

func:
    append_write

"""


def append_write(filename="", text=""):
    """appends text to a file

    Args:
        filename: name of file
        text: text to append

    Returns:
        number of characters written

    """
    num = 0
    with open(filename, "a", encoding="UTF-8") as MyFile:
        num = MyFile.write(text)
    return num
