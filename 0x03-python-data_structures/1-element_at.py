#!/usr/bin/python3

def element_at(my_list, idx):
    item_count = len(my_list)

    if idx < 0 or idx >= item_count:
        return None

    return my_list[idx]
