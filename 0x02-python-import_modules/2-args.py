#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    a = ':'
    if length == 0:
        a = 's.'
    if length > 1:
        a = 's:'
    print("{} argument{}".format(length, a))
    for i in range(1, length + 1):
        print("{}: {}".format(i, argv[i]))
