#!/usr/bin/python3

"""Returns dictionary description of objects"""


def class_to_json(obj):
    """Returns dictionary description of objects
        Args:
            obj: Object
    """

    if hasattr(obj, '__dict__'):
        return obj.__dict__

    return {}
