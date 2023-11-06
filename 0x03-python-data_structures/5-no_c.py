#!/usr/bin/python3
def no_c(my_str):
    new_str = ""
    for i in my_str:
        if i == 'c' or i == 'C':
            continue
        new_str += i
    return new_str
