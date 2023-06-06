#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the Rectangle."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the Rectangle."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x (horizontal offset) of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x (horizontal offset) of the Rectangle."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y (vertical offset) of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y (vertical offset) of the Rectangle."""
        self.__y = value
