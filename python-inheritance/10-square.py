#!/usr/bin/python3
"""
Module 10-square

This module defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square Class

    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: The formatted string representation.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
