#!/usr/bin/python3
"""Custom function to check object's type against a given class."""


def is_same_class(obj, a_class):
    """Check if the type of an object matches the provided class."""
    return type(obj) is a_class
