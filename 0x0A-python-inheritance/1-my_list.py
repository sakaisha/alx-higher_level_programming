#!/usr/bin/python3
"""Defines the MyList class, a subclass of list,
with a method to print the list sorted."""


class MyList(list):
    """create a MyList class"""
    def print_sorted(self):
        """create sort function"""
        print(sorted(self))
