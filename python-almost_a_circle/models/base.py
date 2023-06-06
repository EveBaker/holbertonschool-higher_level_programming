#!/usr/bin/python3
""" This module writes the first class for this project the Base class """

import json


class Base:
    """ Base class will be the 'base' of all other classes in this project. """
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
        return json.dumps(list_dictionaries)

    @classmethod
    def from_json_string(cls, json_string):
        """ Static method that returns the list of the JSON string. """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON representation of a string to a file. """
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
        # create a dummy instance for the respective class to be created
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        # update the dummy instance with the dictionary
        dummy.update(**dictionary)
        # return the created instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances. """
        # create a class name JSON file
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as file:
                # read the file and convert to list of dictionaries
                list_dicts = cls.from_json_string(file.read())
                # convert list of dictionaries to list of instances
                for dictionary in list_dicts:
                    instance = cls.create(**dictionary)
                    instances.append(instance)
        except FileNotFoundError:
            return []
        return instances
