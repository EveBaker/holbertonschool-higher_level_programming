#!/usr/bin/python3

"""
This module defines the Square class, a subclass of Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object.
        """

        self.width = size
        self.height = size
        self.x = x
        self.y = y
        self.id = id
        self.validate_positive_integer(size, "size")
        self.validate_positive_integer(x, "x")
        self.validate_positive_integer(y, "y")

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def display(self):
        """
        Displays a visual representation of the square.
        """

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    @staticmethod
    def validate_positive_integer(value, name):
        """
        Validates if the given value is a positive integer.
        """

        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")
