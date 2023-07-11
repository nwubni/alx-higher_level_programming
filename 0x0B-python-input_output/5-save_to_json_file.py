#!/usr/bin/python3

"""Writes object to text file in JSON format"""

import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file in JSON format
        Args:
            my_obj: Object parameter
            filename: File name to use
    """

    with open(filename, "r") as f:
        json.dumps(my_obj, f)
