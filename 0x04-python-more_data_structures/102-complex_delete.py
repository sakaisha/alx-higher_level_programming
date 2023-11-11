#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    deletekey = []
    for k, x in a_dictionary.items():
        if x == value:
            deletekey += [k]
    for k in deletekey:
        a_dictionary.pop(k)
    return a_dictionary
