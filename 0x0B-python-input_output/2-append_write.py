#!/usr/bin/python3

"""Appends to a file"""


def append_write(filename="", text=""):
    """Appends text to a file
        Args:
            filename: Filename
            text: Text content to append to file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
