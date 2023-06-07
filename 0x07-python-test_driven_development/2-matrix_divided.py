#!/usr/bin/python3

""" 2-matrix_divided module

func1:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """ matrix_divided divides a matrix
    Args:
        matrix: list of list
        div: number to divide by

    Returns:
        new matrix
    """

    check = 0
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(matrix) != list:
        check = 1
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    else:
        L1 = len(matrix)
        L2 = 0
        err = "matrix must be a matrix (list of lists) of integers/floats"
        if len(matrix) >= 1 and isinstance(matrix[0], list):
            L2 = len(matrix[0])
            if L2 == 0:
                raise TypeError(err)
        else:
            raise TypeError(err)
        for i in range(len(matrix)):
            if type(matrix[i]) != list:
                raise TypeError(err)
            if L2 != len(matrix[i]):
                err = "Each row of the matrix must have the same size"
                raise TypeError(err)
            for j in matrix[i]:
                c = [int, float]
                if type(j) not in c:
                    raise TypeError(err)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for i in matrix:
        hold = []
        for j in range(len(i)):
            hold.append(round((i[j] / div), 2))
        new.append(hold)
    return new
