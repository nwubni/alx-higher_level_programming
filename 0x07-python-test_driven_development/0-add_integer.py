#!/usr/bin/python3

"""Module that adds two integer or floating numbers"""


def add_integer(a, b=98):
    """Function that adds two integer or floating numbers
    Args:
        a (int/float): First parameter
        b (int/float): Secode parameter
    Returns:
        Numeric: sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)


print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
