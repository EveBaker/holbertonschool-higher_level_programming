#!/usr/bin/python3
"""
Module: 0-read_file

Description:
    This module defines the read_file function that reads a text file (UTF8) and prints its content to stdout.
"""

def read_file(filename=""):
    """
    Read a text file and print its content to stdout.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
