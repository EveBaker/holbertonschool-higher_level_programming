#!/usr/bin/python3
"""
7-base_geometry.py:
This module provides a class called BaseGeometry.

Classes:
    BaseGeometry:
        Base class for other geometry-related classes.

    Methods:
        area(self):
            Compute the area of the geometry.

            Raises:
                Exception: Always raises an Exception with the message "area() is not implemented".

        integer_validator(self, name, value):
            Validate the value as an integer.

            Args:
                name (str): The name of the value.
                value: The value to be validated.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than or equal to 0.
"""

class BaseGeometry:
    """
    Base class for other geometry-related classes.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
