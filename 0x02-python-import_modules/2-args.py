#!/usr/bin/python3

import sys

argc = len(sys.argv)
arguments = "argument" if (argc - 1) == 1 else "arguments"
arguments += "." if (argc - 1) == 0 else ":"

print("{} {}".format(argc - 1, arguments))

for i in range(1, argc):
    print("{}: {}".format(i, sys.argv[i]))
