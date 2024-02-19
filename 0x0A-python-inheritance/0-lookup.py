#!/usr/bin/python3
"""This module defines a function, lookup(obj),
which returns the list of attributes and methods
available for a given object."""


def lookup(obj):
    """Returns the list of available 
    attributes and methods of an object."""
    return dir(obj)
