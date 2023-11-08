#!/usr/bin/python3
'''writes a string to a text file (UTF8) and
returns the number of characters written'''


def write_file(filename="", text=""):
    '''function to write text to a file'''
    with open(filename, 'w+') as f:
        return f.write(text)
