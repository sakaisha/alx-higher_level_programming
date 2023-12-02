#!/usr/bin/python3
"""Unit tests for the max_integer function.

This module contains a set of unittests for the max_integer function,
which finds the maximum integer in a given list.

Uses the Google docstring style and adheres to PEP 8 style guidelines.

"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max(self):
        """Test max_integer with various input lists."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)  # pycodestyle: E241
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)  # pycodestyle: E241

if __name__ == '__main__':
    unittest.main()
