#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    item_count = len(my_list)

    if idx < 0 or idx >= item_count:
        return my_list

    new_copy = my_list[:]
    new_copy[idx] = element

    return new_copy
