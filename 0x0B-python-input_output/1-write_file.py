#!/usr/bin/python3

"""Writes to a file"""


def write_file(filename="", text=""):
    """Writes text into filename
        Args:
            filename: Filename
            text: Text content to write to file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
