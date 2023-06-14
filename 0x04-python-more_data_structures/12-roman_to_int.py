#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    numerals = {'M': 1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V': 5, 'I': 1}

    ans = 0
    prev = 2000

    for c in roman_string:
        if prev < numerals[c]:
            ans -= prev * 2

        ans += numerals[c]
        prev = numerals[c]

    return ans
