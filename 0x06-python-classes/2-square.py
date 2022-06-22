#!/usr/bin/python3
"""define a Class Square"""


class Square:
    """Represent a squre."""
    def __init__(self, size=0):
        """initialize of attribute
        Args (int): Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
