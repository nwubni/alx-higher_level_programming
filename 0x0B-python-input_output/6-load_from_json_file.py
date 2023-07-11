#!/usr/bin/python3

"""Creates object from file content"""

import json


def load_from_json_file(filename):
    """Creates object from file content
        Args:
            filename: File name to read from
    """

    with open(filename, "r") as f:
        return json.loads(f.read())
