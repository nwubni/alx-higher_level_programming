#!/usr/bin/python3

"""Reads a file"""


def read_file(filename=""):
    """Reads a file and prints its content"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
