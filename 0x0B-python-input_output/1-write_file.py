#!/usr/bin/python3

"""Writes to a file"""


def write_file(filename="", text=""):
    """Writes text into filename"""
    with open(filename, "w") as f:
        f.write(text)

    f.close()
