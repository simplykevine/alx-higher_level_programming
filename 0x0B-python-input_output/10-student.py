#!/usr/bin/python3
'''class that makes a student'''


class Student:
    '''student class'''
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        '''inits the data needed'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dict rep of the data'''
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None or type(attrs) != list:
            return context
        else:
            cont = {}
            for item in attrs:
                if type(item) != str:
                    return context
                if item in context.keys():
                    cont[item] = context[item]
            return cont
