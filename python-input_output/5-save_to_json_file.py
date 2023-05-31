#!/usr/bin/python3
"""
Module: 5-save_to_json_file
This module defines the save_to_json_file function that writes an Object to a text file
using a JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using JSON representation.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
