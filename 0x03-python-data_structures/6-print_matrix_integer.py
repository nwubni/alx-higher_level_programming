#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        r_len = len(row)

        for (i, el) in enumerate(row):
            print("{:d}".format(el), end=' ' if i < (r_len - 1) else '')

        print()
