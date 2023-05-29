#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        length = 0
        if x < 0:
            raise IndexError
        else:
            for i in range(x):
                print(my_list[i], end='')
                length += 1
    except IndexError:
        pass
    finally:
        print()
        return length
