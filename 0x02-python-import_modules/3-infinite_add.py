#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if (length - 1) == 0:
        print('0')
    else:
        total = 0
        for i in range(1, length):
            total += int(argv[i])
        print(total)
