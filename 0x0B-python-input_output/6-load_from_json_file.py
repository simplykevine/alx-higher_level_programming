#!/usr/bin/python3
'''Write a function that creates an Object from a '''


import json


def load_from_json_file(filename):
    '''Function that does the work'''
    with open(filename, 'r') as f:
        return json.load(f)
