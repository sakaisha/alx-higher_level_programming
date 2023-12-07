#!/usr/bin/python3
"""Module to calculate the number of lines in a file."""


def number_of_lines(filename=""):
    """Return the number of lines in the specified file."""
    ct = 0
    with open(filename, 'r') as f:
        for line in f:
            ct += 1
    return ct
