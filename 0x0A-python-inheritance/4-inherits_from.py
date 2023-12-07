#!/usr/bin/python3
"""Check inheritance between objects and classes."""


def inherits_from(obj, a_class):
    """Check if obj is a subclass of a_class."""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
