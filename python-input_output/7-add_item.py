#!/usr/bin/python3
"""
Module: 7-add_item

Description:
    This module provides a script that adds all command-line arguments to a Python list and saves them to a file.
File Output:
    The arguments are saved as a JSON representation in a file named "add_item.json". If the file already exists, the items are appended to it.
"""

import sys
import json
from typing import List


def add_items_to_list(filename: str, items: List[str]):
    """
    Add items to a Python list and save it to a file.
    """
    my_list = []

    # Load existing list from file if it exists
    try:
        with open(filename, 'r') as file:
            my_list = json.load(file)
    except FileNotFoundError:
        pass

    # Add new items to the list
    my_list.extend(items)

    # Save the updated list to the file
    with open(filename, 'w') as file:
        json.dump(my_list, file)


if __name__ == "__main__":
    # Remove the script name from the arguments
    arguments = sys.argv[1:]

    # Add items to the list and save to file
    add_items_to_list("add_item.json", arguments)
