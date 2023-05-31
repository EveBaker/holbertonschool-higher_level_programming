#!/usr/bin/python3
"""
Module: 2-append_write

Description:
    This module defines the append_write function that appends a string to a text file (UTF8)
    and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    
    return num_characters_added
