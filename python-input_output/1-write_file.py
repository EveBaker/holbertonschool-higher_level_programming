#!/usr/bin/python3
"""
Module: 1-write_file

Description:
    This module defines the write_file function that writes a string to a text file (UTF8) and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
