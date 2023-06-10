#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    item_count = len(my_list)

    if idx >= 0 and idx < item_count:
        del my_list[idx]

    return my_list
