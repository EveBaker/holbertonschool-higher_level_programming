#!/usr/bin/python3

"""
This module defines the Square class, which represents a square shape.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.
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
        self.validate_integer(size, 'size')
        self.validate_integer(x, 'x')
        self.validate_integer(y, 'y')

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.width * self.height

    def display(self):
        """
        Prints a visual representation of the square using '#' characters.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    @staticmethod
    def validate_integer(value, name):
        """
        Validates if the given value is a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")


