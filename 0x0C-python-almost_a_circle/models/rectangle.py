#!/usr/bin/python3
"""Defines the class Rectangle."""


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a Rectangle.

        Args:
            width: Width of the rectangle
            heigth: Heigth of the rectangle
            x: The x coordinate of the rectangle
            y: The y coordinate of the rectangle
            id: id
        """

        self.width = width
        self.heigth = heigth
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""

        self.__width = value

    @property
    def heigth(self):
        """Retrieves the heigth attribute."""

        return self.__heigth

    @heigth.setter
    def heigth(self, value):
         """Sets the heigth attribute."""

         self.__heigth = value

    @property
    def x(self):
        """Retrieves the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""

        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""

        self.__y = value
