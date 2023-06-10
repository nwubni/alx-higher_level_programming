#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]

    for i, e in enumerate(tuple_a):
        res[i] += e

    for i, e in enumerate(tuple_b):
        res[i] += e

    return (res[0], res[1])
