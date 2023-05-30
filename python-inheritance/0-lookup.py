#!/usr/bin/python3
"""
0-lookup.py:
This module provides a function to retrieve the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object to look up.

    Returns:
        list: A list of attribute and method names of the object.
    """
    return dir(obj)