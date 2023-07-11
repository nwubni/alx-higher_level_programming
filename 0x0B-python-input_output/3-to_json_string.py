#!/usr/bin/python3

"""Converts Object JSON"""

import json


def to_json_string(my_obj):
    """Converts Object to JSON
        Args:
            my_obj: Object to convert
        Returns:
            The JSON representation of my_obj
    """

    return json.dumps(my_obj)
