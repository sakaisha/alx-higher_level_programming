#!/usr/bin/python3
def complex_delete(a_dictionary, xalue):
    deletekey = []
    for k, x in a_dictionary.items():
        if x == xalue:
            deletekey += [k]
    for k in deletekey:
        a_dictionary.pop(k)
    return a_dictionary
