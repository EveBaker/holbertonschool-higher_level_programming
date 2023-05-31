#!/usr/bin/python3
"""
7-base_geometry.py:
This module provides a class called BaseGeometry.

    BaseGeometry:
        Base class for other geometry-related classes.
        area(self):
            Compute the area of the geometry.

            Raises:
                Exception: Always raises an Exception with the message "area() is not implemented". """

class BaseGeometry:
    """
    Base class for other geometry-related classes.
    """

    def area(self):
        """
        Compute the area of the geometry.
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
      
    if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
