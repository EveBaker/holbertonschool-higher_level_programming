#!/usr/bin/python3
"""
4-inherits_from.py:
This module provides a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

Functions:
Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
    Returns:
        True if the object is an instance of a class that inherited from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
