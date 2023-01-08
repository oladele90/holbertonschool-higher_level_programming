#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = abs(number) % 10
str = ""
if number < 0:
    number2 = -number2
if number2 == 0:
    str = ("0")
elif number2 < 5:
    str = ("less than 6 and not 0")
else:
    str = ("greater than 5")
print("Last digit of {} is {} and is {}".format(number, number2, str))