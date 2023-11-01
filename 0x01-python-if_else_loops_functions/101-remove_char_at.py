#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str_updated = ""
    for c in str:
        if i != n:
            str_updated += c
        i += 1
    return str_updated
