#!/usr/bin/python3
"""
Module: 6-load_from_json_file

This module defines the load_from_json_file function that creates an Object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Create an Object from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
