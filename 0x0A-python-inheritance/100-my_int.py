#!/usr/bin/python3
"""Module defining MyInt class to compare integers."""


class MyInt(int):
    """A class to compare to integer values."""

    def __init__(self, value):
        """Initialize attribute with a given value."""
        self.value = value

    def __str__(self):
        """Return the string representation of the value."""
        return str(self.value)

    def __eq__(self, other):
        """Compare two integer values for inequality."""
        return self.value != other

    def __ne__(self, other):
        """Compare two integer values for equality."""
        return self.value == other
