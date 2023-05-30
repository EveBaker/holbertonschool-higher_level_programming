#!/usr/bin/python3
class Base:
    """My base class"""

    __nb_instances = 0

    def __init__(self):
        """Initialize Base instance"""
        Base.__nb_instances += 1
        self.id = Base.__nb_instances


class User(Base):
    """My User class"""

    def __init__(self):
        """Initialize User instance"""
        super().__init__()
        self.id += 99


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj (object): The object to look up.

    Returns:
        list: A list of attribute and method names of the object.
    """
    return dir(obj)
