#!/usr/bin/python3

def weight_average(my_list=[]):
    sum = 0
    weights = 0

    for t in my_list:
        sum += t[0] * t[1]
        weights += t[1]

    return sum / weights
