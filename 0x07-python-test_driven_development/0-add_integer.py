#!/usr/bin/python3
"""Defines an integer addition function."""

'''
File_name: 0-add_integer.py
Created: 30-OCT-2023
Author: UMUTONI Kevine (simplykevine)
Project name: 0x07-python-test_driven_development
'''
try:
        if not (isinstance(a, int)) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif not (isinstance(b, int)) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            if isinstance(a, float) or isinstance(b, float):
                return (int(a) + int(b))
            return a + b
    except Exception as e:
        return (e)
