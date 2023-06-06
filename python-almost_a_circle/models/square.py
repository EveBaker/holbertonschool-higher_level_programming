#!/usr/bin/python3
""" This module writes the class Square that inherits from Rectangle class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square, which is a special type of rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square object.
        """
        self.width = size
        self.height = size
        self.x = x
        self.y = y
        self.id = id

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
