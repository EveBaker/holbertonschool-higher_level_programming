#!/usr/bin/python3
"""
This module defines the Base class, which serves as the base for all other classes.
"""

import json

class Base:
    """Base class for managing id attribute and providing utility methods."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance with an optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a list of objects to a file."""
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a class with attribute values already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
