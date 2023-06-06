#!/usr/bin/python3

def remove_char_at(str, n):
    res = ""
    i = 0

    for c in str:
        if i == n:
            i += 1
            continue

        res += c
        i += 1

    return res
