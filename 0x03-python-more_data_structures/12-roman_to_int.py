#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {"M": 1000, "D": 500, "C": 100, "L": 50,
               "X": 10, "V": 5, "I": 1}
    sum = 0
    if not roman_string or cond is None:
        return 0
    for i in roman_string:
        if i in my_dict:
            sum += my_dict[i]
    return sum
