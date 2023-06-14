#!/usr/bin/python3

"""12-pascal_triangle module

func:
    pascal_triangle

"""


def pascal_triangle(n):
    """eturns a list of lists of integers
    representing the Pascal’s triangle

    Args:
        n: size of triangle

    Returns:
        list of lists

    """

    main = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        first = 0
        second = main[i - 1][0]
        new = []
        for j in range(len(main[i - 1])):
            new.append(first + second)
            first = main[i - 1][j]
            if (j + 1) == len(main[i - 1]):
                second = 0
            else:
                second = main[i - 1][j + 1]
        new.append(first + second)
        main.append(new)
    return main
