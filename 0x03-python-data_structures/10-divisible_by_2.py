#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    res = []

    for el in my_list:
        if el & 1 == 0:
            res.append(True)
            continue

        res.append(False)

    return res
