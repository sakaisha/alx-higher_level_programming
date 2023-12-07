#!/usr/bin/python3
"""Module to read lines from a text file."""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file.

    Args:
        filename: Name of the file.
        nb_lines: Number of lines to be printed.

    Returns:
        Content of line(s).
    """
    i = 1
    with open(filename, 'r') as f:
        for line in f:
            if i <= nb_lines or nb_lines < 1:
                print(line, end='')
                i += 1
