#!/usr/bin/python3
"""
Script: 7-add_item

This script adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_arguments_to_list(filename, arguments):
    """
    Add arguments to a Python list and save them to a file.

    Args:
        filename (str): The name of the file to save the list.
        arguments (list): List of arguments to add.

    Returns:
        None
    """
    # Check if the file exists
    if path.exists(filename):
        # Load the existing list from the file
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add the arguments to the list
    my_list.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)


def main():
    # Name of the file to save the list
    filename = "add_item.json"

    # Arguments passed to the script (excluding the script name itself)
    arguments = sys.argv[1:]

    # Add the arguments to the list and save them to the file
    add_arguments_to_list(filename, arguments)


if __name__ == "__main__":
    main()
