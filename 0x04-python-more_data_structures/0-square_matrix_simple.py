#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = []

    for m in matrix:
        res.append(list(map(lambda x: x ** 2, m)))

    return res
