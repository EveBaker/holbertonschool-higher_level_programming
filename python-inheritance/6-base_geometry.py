"""
6-base_geometry.py:
This module provides a class called BaseGeometry.

Classes:
    BaseGeometry:
        Base class for other geometry-related classes.

    Methods:
        area(self):
            Compute the area of the geometry.

            Raises:
                Exception: Always raises an Exception with the message "area() is not implemented".
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
