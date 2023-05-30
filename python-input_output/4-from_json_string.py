#!/usr/bin/python3
"""
Module: 4-from_json_string

This module defines the from_json_string function that returns an object (Python data structure)
represented by a JSON string.
"""

import json

def from_json_string(my_str):
    """
    Return an object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        obj: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
