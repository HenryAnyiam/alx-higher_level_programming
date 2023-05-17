#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        keys = list(roman.keys())
        for i in reversed(range(len(roman_string) - 1)):
            if roman_string[i] not in roman:
                return 0
            if keys.index(roman_string[i]) < keys.index(roman_string[i + 1]):
                num -= roman[roman_string[i]]
            else:
                num += roman[roman_string[i]]
        num += roman[roman_string[-1]]
        return num
    return 0
