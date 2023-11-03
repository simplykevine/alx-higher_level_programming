#!/usr/bin/python3
"""A function to sperate words in python"""
'''
File_name: 0-rectangle.py
Created: 5-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Size: Large
Project: 0x08-python-more_classes
Status: Not yet submitted.
'''


def text_indentation(text):
    '''Fucntion to bring the texts'''
    if type(text) != str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)]
        )

    print("{}".format(text), end="")
