#!/usr/bin/python3
import random
number = random.randint(-10, 10)
tmp = "{0} is {1}"
output = ""

if number == 0:
    output = tmp.format(number, "zero")
elif number > 0:
    output = tmp.format(number, "positive")
else:
    output = tmp.format(number, "negative")

print(output)
