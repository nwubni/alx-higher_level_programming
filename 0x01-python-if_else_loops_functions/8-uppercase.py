#!/usr/bin/python3

def uppercase(str):
    output = ""

    for c in str:
        code = ord(c)

        if code >= 97 and code <= 122:
            output += chr(code - 32)
            continue

        output += c

    print("{}".format(output))
