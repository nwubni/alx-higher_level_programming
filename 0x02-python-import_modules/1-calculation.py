#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    output = "{0} {2} {1} = {3}"

    print(output.format(a, b, '+', add(a, b)))
    print(output.format(a, b, '-', sub(a, b)))
    print(output.format(a, b, '*', mul(a, b)))
    print(output.format(a, b, '/', div(a, b)))
