#!/usr/bin/python3

def max_integer(my_list=[]):
    item_count = len(my_list)

    if not my_list or item_count == 0:
        return None

    ans = -1000000000

    for el in my_list:
        if el > ans:
            ans = el

    return ans
