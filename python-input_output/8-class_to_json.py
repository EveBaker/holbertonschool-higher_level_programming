"""Class to JSON Module

This module provides a function to convert an object to a dictionary representation
with a simple data structure suitable for JSON serialization.

"""

def class_to_json(obj):
    """Converts an object to a dictionary representation for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary representation of the object.

    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    else:
        return obj
