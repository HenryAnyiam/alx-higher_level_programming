#!/usr/bin/python3

""" 100-matrix_mul.py module

func1:
    matrix_mul
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiples two matrix

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        new matrix

    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of list")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_b should contain only integers or floats")
    la = len(m_a[0])
    for i in m_a:
        if la != len(i):
            raise TypeError("each row of m_a must be of the same size")
    lb = len(m_b[0])
    for i in m_b:
        if lb != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return numpy.matmul(m_a, m_b)
