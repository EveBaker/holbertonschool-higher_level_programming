#!/usr/bin/python3
"""
2-is_same_class.py:
This module provides a function to check if an object is exactly an instance of a specified class.

Functions:
    is_same_class(obj, a_class):
        Returns True if the object is exactly an instance of the specified class, otherwise False.

"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) is a_class
