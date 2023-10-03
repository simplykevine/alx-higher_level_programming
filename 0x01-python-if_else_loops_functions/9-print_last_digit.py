#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ldigit = abs(number) % 10
    else:
        ldigit = number % 10
    print("{:d}".format(ldigit), end="")
    return ldigit
