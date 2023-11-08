#!/usr/bin/python3
''' writes a string to a text file (UTF8) and
returns the number of characters written
'''


def number_of_lines(filename=""):
    ''' function: number_of_lines
    '''
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter
