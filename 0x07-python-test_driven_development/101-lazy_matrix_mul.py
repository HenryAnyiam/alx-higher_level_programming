#!/usr/bin/python3

""" 101-lazy_matrix_mul.py module

func1:
    lazy_matrix_mul
"""

import numpy


def lazy_matrix_mul(m_a=[[1]], m_b=[[1]]):
    """multiples two matrix

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        new matrix

    """
    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    h_a = len(m_a)
    w_a = 0 if h_a == 0 else len(m_a[0])
    h_b = len(m_b)
    w_b = 0 if h_b == 0 else len(m_b[0])
    err = f"shapes ({w_b},{h_a}) and ({w_b},{w_b}) not aligned"
    err += f": {h_a} (dim {h_b}) != {w_b} (dim {h_a})"
    if h_a == 0 or w_a == 0 or h_b == 0 or w_b == 0:
        raise ValueError(err)
    for r_a in m_a:
        if len(r_a) != len(m_a[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_a in r_a:
            if type(c_a) is not int and type(c_a) is not float:
                raise TypeError("invalid data type for einsum")
    for r_b in m_b:
        if len(r_b) != len(m_b[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_b in r_b:
            if type(c_b) is not int and type(c_b) is not float:
                raise TypeError("invalid data type for einsum")
    if len(m_a[0]) != len(m_b):
        raise ValueError(err)
    return numpy.matmul(m_a, m_b)
