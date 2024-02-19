#!/usr/bin/python3
"""Defines a function to add an attribute to an object."""


def add_attribute(obj, key, value):
    """Adds a new attribute to the object if possible."""
    if '__dict__' in dir(obj):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
