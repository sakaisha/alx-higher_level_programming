#!/usr/bin/python3
"""Custom utilities for class checking."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if  object is an inst of specified class, otherwise False.
    """
    return isinstance(obj, a_class)
