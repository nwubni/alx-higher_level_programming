#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    operators = "+-*/"

    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    op = sys.argv[2]

    if not (op in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ans = 0

    if op == '+':
        ans = add(a, b)
    elif op == '-':
        ans = sub(a, b)
    elif op == '*':
        ans = mul(a, b)
    else:
        ans = div(a, b)

    print("{} {} {} = {}".format(a, op, b, ans))
