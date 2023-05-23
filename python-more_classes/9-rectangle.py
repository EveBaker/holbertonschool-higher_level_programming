#!/usr/bin/python3

"""
This module defines a Rectangle class that represents a rectangle by its width and height.
"""

class Rectangle:
    """
    Represents a rectangle by its width and height.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle class with optional width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return str(self.print_symbol) * self.width + "\n" * self.height

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when the rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with equal width and height.
        """
        return cls(size, size)
