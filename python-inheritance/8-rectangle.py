#!/usr/bin/python3
"""
Module 8-rectangle

This module defines the Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle Class

    Represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        String representation of the Rectangle instance.

        Returns:
            str: The formatted string representation.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
