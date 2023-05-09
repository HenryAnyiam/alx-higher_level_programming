#!/usr/bin/python3
for i in range(26, 0, -1):
    j = i + 64
    if j % 2 == 0:
        j = i + 96
    print("{}".format(chr(j)), end="")
