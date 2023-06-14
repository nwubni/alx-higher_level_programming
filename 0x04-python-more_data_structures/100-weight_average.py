#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0

    sum = 0
    weights = 0

    for t in my_list:
        sum += t[0] * t[1]
        weights += t[1]

    return sum / weights
