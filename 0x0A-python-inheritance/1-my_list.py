#!/usr/bin/python3
"""Defines classe MyList qui hérite de list"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints the list"""
        print(sorted(self))
