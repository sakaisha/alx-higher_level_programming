#!/usr/bin/python3
"""Defines a function to check if an object
inherits from a specified class."""


def inherits_from(obj, a_class):
    """is sub_class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
