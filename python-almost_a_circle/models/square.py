#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
