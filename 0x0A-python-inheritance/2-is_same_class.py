#!/usr/bin/python3

"""Checks if classes are the same"""


def is_same_class(obj, a_class):
    """Function that checks if 
    two classes are the same
    """
    is_inst = isinstance(obj, a_class)
    obj_type = type(obj)
    return is_inst and obj_type == a_class
