#!/usr/bin/python3
"""Module to perform object lookup."""


def lookup(obj):
    """Returns a list of attributes and methods of the input object."""
    return dir(obj)
