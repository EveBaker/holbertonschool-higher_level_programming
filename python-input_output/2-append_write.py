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

    Args:
        filename (str): The name of the text file (default is an empty string).
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    
    return num_characters_added
