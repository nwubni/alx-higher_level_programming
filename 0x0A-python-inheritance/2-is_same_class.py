#!/usr/bin/python3

"""Checks if classes are the same"""


def is_same_class(obj, a_class):
    """Function that checks if 
    two classes are the same
    """
    return isinstance(obj, a_class) and type(obj) == a_class
