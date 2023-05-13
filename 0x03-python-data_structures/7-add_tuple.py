#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, c, d = (0, 0, len(tuple_a), len(tuple_b))
    if c > 0:
        a = tuple_a[0]
    if d > 0:
        a += tuple_b[0]
    if c > 1:
        b = tuple_a[1]
    if d > 1:
        b += tuple_b[1]
    return (a, b)
