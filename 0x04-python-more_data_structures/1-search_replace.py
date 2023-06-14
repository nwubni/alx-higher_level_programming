#!/usr/bin/python3

def search_replace(my_list, search, replace):
    res = []

    for el in my_list:
        if el == search:
            res.append(replace)
            continue

        res.append(el)

    return res
