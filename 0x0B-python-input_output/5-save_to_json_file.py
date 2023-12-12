#!/usr/bin/python3
'''A function that reads a json file'''


import json


def save_to_json_file(my_obj, filename):
    '''saves a doc to a json format'''
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
