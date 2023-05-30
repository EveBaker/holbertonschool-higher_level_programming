#!/usr/bin/python3
"""
Module: 6-load_from_json_file

This module defines the load_from_json_file function that creates an Object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Create an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
