#!/usr/bin/python3
def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    maxm = 0
    person = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > maxm:
                maxm = a_dictionary[key]
                person = key
    return person
