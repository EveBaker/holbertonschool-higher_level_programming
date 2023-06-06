#!/usr/bin/python3
""" This module writes the first class for this project the Base class """

import json


class Base:
    """ Base class will be the “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor for Base class with optional id attribute. """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation
        of list_dictionaries. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        # Check the type of objects in the list
        obj_type = type(list_dictionaries[0])

        # Convert each object to its dictionary representation
        dict_list = [obj.to_dictionary() for obj in list_dictionaries]

        # Serialize the dictionary list based on the object type
        if obj_type.__name__ in ["Rectangle", "Square"]:
            return json.dumps([obj.__dict__ for obj in list_dictionaries])
        else:
            return json.dumps(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """ Static method that Returns: the list of the JSON string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method writes the JSON representation of a string to a file. """
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        # convert list objects to list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        # convert list dictionaries to json string
        json_str = cls.to_json_string(list_dicts)
        # write the JSON string to a file
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance of a class. """
        # create a dummy instance for either cls to be created
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        # update the dummy instance with the dictionary
        dummy.update(**dictionary)
        # we created the instance of the class with all attrs set
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that Returns: A list of instances. """
        # create a class name JSON file
        filename = cls.__name__ + ".json"
        # try to open the file
        try:
            with open(filename, "r") as file:
                # read the file and convert to list of dictionaries
                list_dicts = cls.from_json_string(file.read())
                # convert list of dictionaries to list of instances
                return [cls.create(**dictionary) for dictionary in list_dicts]
        # if empty file or file does not exist return empty list
        except FileNotFoundError:
            return []
