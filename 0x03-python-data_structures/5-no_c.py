#!/usr/bin/python3

def no_c(my_string):
    output = ""

    for c in my_string:
        if c in "cC":
            continue

        output += c

    return output
