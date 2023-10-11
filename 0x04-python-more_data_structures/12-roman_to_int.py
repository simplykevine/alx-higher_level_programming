#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    strg = list(roman_string[::-1].upper())
    flag = 1
    sum = 0
    for l in range(len(strg) - 1):
        sum = sum + numerals[strg[l]]*flag
        if numerals[strg[l]] <= numerals[strg[l + 1]]:
            flag = 1
        if numerals[strg[l]] > numerals[strg[l + 1]]:
            flag = -1
    if flag == 1:
        sum = sum + numerals[strg[len(strg) - 1]]
    if flag == -1:
        sum = sum - numerals[strg[len(strg) - 1]]
    return sum
