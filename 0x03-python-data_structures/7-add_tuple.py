#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]

    for i in range(min(len(tuple_a), 2)):
        res[i] += tuple_a[i]

    for i in range(min(len(tuple_b), 2)):
        res[i] += tuple_b[i]

    return tuple(res)
