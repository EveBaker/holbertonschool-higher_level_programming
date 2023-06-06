#!/usr/bin/python3
""" This module writes the first class for this project, the Base class """

import json


class Base:
    """ Base class will be the "base" of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor for Base class with an optional id attribute. """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation
        of a list of dictionaries. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def from_json_string(cls, json_string):
        """ Static method that returns the list from the JSON string. """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON representation of a list of objects to a file. """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        # Convert list of objects to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        # Convert list of dictionaries to a JSON string
        json_str = cls.to_json_string(list_dicts)
        # Write the JSON string to a file
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance of a class. """
        # Create a dummy instance of the class
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        # Update the dummy instance with the dictionary
        if dummy:
            dummy.update(**dictionary)
        # Return the created instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances from a JSON file. """
        # Create a JSON file name
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                # Read the file and convert to a list of dictionaries
                list_dicts = cls.from_json_string(file.read())
                # Create a list of instances from the list of dictionaries
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
