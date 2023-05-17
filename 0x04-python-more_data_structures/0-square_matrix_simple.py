#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if type(matrix) == list:
        return [list(map((lambda x: x * x), i)) for i in matrix]
