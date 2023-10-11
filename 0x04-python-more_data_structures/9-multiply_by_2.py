#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2 """
    return {k: 2 * v for k, v in a_dictionary.items()}
