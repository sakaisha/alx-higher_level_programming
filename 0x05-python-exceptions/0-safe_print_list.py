#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    new_str = ""
    for el in my_list[:x]:
        new_str += str(el)
        n += 1
    try:
        print(new_str)
        return n
    except:
        print("Error")
