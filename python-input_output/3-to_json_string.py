#!/usr/bin/python3
"""
Module: 3-to_json_string

This module defines the to_json_string function that returns the JSON representation
of an object (string).
"""

import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object.
    """
    return json.dumps(my_obj)
