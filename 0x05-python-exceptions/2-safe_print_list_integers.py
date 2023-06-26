#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_prints = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            num_prints += 1
        except (TypeError, ValueError):
            continue

    print()
    return num_prints
