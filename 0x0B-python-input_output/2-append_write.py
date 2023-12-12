#!/usr/bin/python3
'''appends a string at the end of a text file and returns the
number of characters added:
'''


def append_write(filename="", text=""):
    '''function to write text to a file'''
    with open(filename, 'a+') as f:
        return f.write(text)
