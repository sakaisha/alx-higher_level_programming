#!/usr/bin/python3

"""Module: say_my_name - Print first name and last name.

Usage:
    This module provides a function say_my_name for printing names.

    Example:
        say_my_name("John", "Doe")

Args:
    first_name (str): String of the first name.
    last_name (str): String of the last name. Defaults to an empty string.

Returns:
    None

Raises:
    TypeError: If first_name or last_name is not a string.

"""

def say_my_name(first_name, last_name=""):
    """Print name following the format: My name is [first_name] [last_name]."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
