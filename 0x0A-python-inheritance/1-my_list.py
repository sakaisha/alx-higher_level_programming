#!/usr/bin/python3
"""A custom list class."""


class MyList(list):
    """Create a MyList class."""

    def print_sorted(self):
        """Print a sorted version of the list."""
        print(sorted(self))
