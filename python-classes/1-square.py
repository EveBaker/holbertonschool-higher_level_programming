#!/usr/bin/python3
"""
Square module.
This module cobtains a class that defines a square"""


class Square:
    """
    Represents a square.
    Attributes:
    __size (int): The size of the square.
    """


def __init__ (self,size):
    """
    Initializes a Square instance.
    Args:
    size (int): The size of the square.
    """
    self.__size = size



def dict_(self):
    """
    Retrieves the dictionary representation of the Square instance.
    Returns:
    dict: The dictionary representation containing the size.
    """
    return {'size': self.__size}


mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)


mysquare = Square(89)
print(type(mysquare))
print(mysquare.dict_)


try:
    print(mysquare.size)
except Exception as e:
    print(e)


mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)


try:
    print(type(mysquare))
except Exception as e:
    print(e)