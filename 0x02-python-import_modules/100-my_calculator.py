#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    operators = "+-*/"

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if not sys.argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    ans = 0

    match op:
        case '+':
            ans = add(a, b)
        case '-':
            ans = sub(a, b)
        case '*':
            ans = mul(a, b)
        case _:
            ans = div(a, b)

    print("{} {} {} = {}".format(a, op, b, ans))
