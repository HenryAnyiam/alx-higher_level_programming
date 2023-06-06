#!/usr/bin/python3

""" 5-text_indentation module

functions:
    text_indentation

"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text

    """
    if type(text) != str:
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while i < length and text[i] == " ":
        i += 1
    chars = ['.', '?', ':']
    new = ""
    while (i < length):
        if text[i] in chars:
            new += text[i] + '\n' + '\n'
            while i < length:
                i += 1
                if i < length and text[i] == " ":
                    pass
                else:
                    i -= 1
                    break
        else:
            new += text[i]
        i += 1
    length = len(new)
    for i in reversed(range(len(new))):
        if new[i] == " ":
            length -= 1
        else:
            break
    New = ""
    for i in range(length):
        New += new[i]
    print(f"{New}", end="")
