#!/usr/bin/python3

def best_score(a_dictionary):
    best = -1000000
    key = None

    if a_dictionary:
        for k, v in a_dictionary.items():
            if v >= best:
                best = v
                key = k

    return key
