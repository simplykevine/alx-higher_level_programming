#!/usr/bin/python3
'''This file creates a my class list '''


class MyList(list):
    '''This Class inherits the built in function list'''

    def print_sorted(self):
        '''Prints the list made in a sorted order  '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
