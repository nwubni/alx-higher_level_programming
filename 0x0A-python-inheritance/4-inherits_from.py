#!/usr/bin/python3

"""Compares two variables for inheritance"""


def inherits_from(obj, a_class):
    """Compares if obj is sub-class fo a_class
        Args:
            obj: Param 1
            a_class: Param 2
    """
    return issubclass(type(obj), a_class) and \
        type(obj) != a_class
