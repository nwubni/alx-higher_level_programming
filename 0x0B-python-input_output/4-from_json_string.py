#!/usr/bin/python3

"""Makes Python object from JSON string"""
import json


def from_json_string(my_str):
    """Makes Python object from JSON string
        Args:
            my_str: String to process
        Returns:
            Python object from my_str
    """

    return json.loads(my_str)
