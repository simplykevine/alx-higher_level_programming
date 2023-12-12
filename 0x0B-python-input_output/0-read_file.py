#!/usr/bin/python3
<<<<<<< HEAD
'''A python script that executes the contents of a file'''
=======
'''A python script that can execute the contents of a file'''
>>>>>>> ac29d63cff334bbaa7e293fd5b23ae2277de8381


def read_file(filename=""):
    '''Reads the data from outside file '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
