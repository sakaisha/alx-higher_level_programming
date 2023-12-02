#!/usr/bin/python3
"""Module for finding the maximum integer in a list."""

def max_integer(lst=[]):
    """Find and return the max integer in a list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        int: Maximum integer in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
