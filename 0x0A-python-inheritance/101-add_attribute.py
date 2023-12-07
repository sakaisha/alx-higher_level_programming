#!/usr/bin/python3

"""
Module to add attributes to objects dynamically.
"""


def add_attribute(obj, key, value):
    """Add attribute to object if possible."""
    """
    Adds a new attribute to the object if it supp dynamic attribute assignment.

    Args:
        obj: Object to which the attribute is to be added.
        key: Key for the new attribute.
        value: Value to be assigned to the new attribute.

    Raises:
        TypeError: If the object does not support dynamic attribute assignment.
    """
    if '__dict__' in dir(obj):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
