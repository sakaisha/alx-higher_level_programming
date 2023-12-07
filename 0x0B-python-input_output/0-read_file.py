#!/usr/bin/python3
"""This module reads a file and prints its content."""


def read_file(filename=""):
    """Reads the content of a file and prints it.

    Args:
        filename (str): name of the file to be read. Defaults to an empty str
    """
    with open(filename, 'r') as f:
        readfile = f.read()
    print(readfile, end="")
