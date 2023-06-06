#!/usr/bin/python3
""" This module writes the class Square that inherits from Rectangle class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class that inherits from Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
            super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
