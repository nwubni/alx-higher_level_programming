#!/usr/bin/python3

for c in range(122, 96, -1):
    print("{}".format(chr(c if c % 2 == 0 else (c - 32))), end='')
