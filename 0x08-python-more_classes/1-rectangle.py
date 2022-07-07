#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """class rectangle."""

    def __init__(self, width=0, height=0):
        """Initalizes a Rectangle instance.

        Args:
            width: width of the rectangle
            heigth: heigth of the rectangle
        """
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance

        Args:
            value: value of the width, must be positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        "Retrieves the heigth of a Rectangle instance"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """Sets the height of a Rectangle instance

        Args:
            value: value of the heigth, must be positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value
