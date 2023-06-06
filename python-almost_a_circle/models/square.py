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

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The unique identifier of the square. Defaults to None.

        Raises:
            ValueError: If size, x, or y is not a positive integer.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
