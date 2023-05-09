#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n < 0 or n > length:
        new = str
        return new
    new = ''
    for i in range(length):
        if i == n:
            continue
        new = new + str[i]
    return new
