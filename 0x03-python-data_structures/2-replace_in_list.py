#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    item_count = len(my_list)

    if idx >= 0 or idx < item_count:
        my_list[idx] = element

    return my_list
