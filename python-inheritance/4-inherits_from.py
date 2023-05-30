#!/usr/bin/python3
"""
4-inherits_from.py:
This module provides a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

Functions:
    inherits_from(obj, a_class):
        Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
