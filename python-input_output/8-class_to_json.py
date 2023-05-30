#!/usr/bin/python3
"""Module 8-class_to_json

This module provides a function to convert an object of a class to a JSON-serializable dictionary.
"""

def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serialized attributes of the object.
    """
    if not hasattr(obj, "__dict__"):
        return {}

    json_dict = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("__"):
            json_dict[key] = value

    return json_dict
