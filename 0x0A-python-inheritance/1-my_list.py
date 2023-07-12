#!/usr/bin/python3

"""Custom List Class"""


class MyList(list):
    """Custom List Class"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
