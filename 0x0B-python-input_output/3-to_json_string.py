#!/usr/bin/python3

import json

"""Converts Object JSON"""


def to_json_string(my_obj):
    """Converts Object to JSON
        Args:
            my_obj: Object to convert
        Returns:
            The JSON representation of my_obj
    """

    return json.dumps(my_obj)
