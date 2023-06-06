#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = "Last digit of {} is {} and is {}"
digit_desc = ""
last_digit = abs(number) % 10

if number < 0:
    last_digit *= -1

if last_digit == 0:
    digit_desc = "0"
elif last_digit > 5:
    digit_desc = "greater than 5"
else:
    digit_desc = "less than 6 and not 0"

print(output.format(number, last_digit, digit_desc))
