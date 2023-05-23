#!/usr/bin/python3
"""
Module: 1-rectangle
Rectangle class with private attributes and properties
"""
class Rectangle:
    """
    Rectangle class
    """
def __init__(self, width=0, height=0):
    """
    Initalization method
    """
    self.width = width
    self.height = height
@property
def width(self):
    """
    Getter method for width
    """
    return self.__width
@width.setter
def width(self, value):
    """
    Setter method for width
    """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value