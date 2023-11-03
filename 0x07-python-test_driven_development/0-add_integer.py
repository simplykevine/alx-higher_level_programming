#!/usr/bin/python3
"""Defines an integer addition function."""

'''
File_name: 0-add_integer.py
Created: 30-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Project name: 0x07-python-test_driven_development
'''

def add_integer(a, b=98):
    ''' Function that adds two integers
    Args:
        a : this must be either an integer or float
        b : Must be either an integer or float, and if not provided
            it takes the defualt value of 98
    Returns:
        an integer: the addition of a and b
    '''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
