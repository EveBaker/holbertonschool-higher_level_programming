#!/usr/bin/python3
"""
3-is_kind_of_class.py:
This module provides a function to check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

Functions: Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class. 
     returns: True if the object is an instance of the object."""
    return isinstance(obj, a_class)

