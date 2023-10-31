#!/usr/bin/python3
"""overriding the '__setattr__' method
"""


'''
File_name: 101-locked_class.py
Created: 6th of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x09-python-everything_is_object
Status: submitted.
'''


class LockedClass:
    """
    # Write a class LockedClass with no class or object attribute, that
    # prevents the user from dynamically creating new instance attributes,
    # except if the new instance attribute is called first_name..
    # VARIABLE(" "):
    # Locked Class Attributes(str): Low memory cost
    # Return: Always 0, (Success).
    """

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
        else:
            object._setattr__(self, name, value)
