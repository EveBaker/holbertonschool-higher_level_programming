#!/usr/bin/python3
"""
1-square module
This module defines the Square class, which represents a square.
"""


class Square:
    """
    Square class
    This class represents a square
    """


def __init__(self,size):
    """
    Initalizes an instance of the square class.
    """
    self.__size = size


def size(self):
    """
    Getter method for the size of the attribute.
    """
    return self.__size


def dict_(self):
    """
    Getter method to retrieve the square attributes as a dictionary.
    """
    return self.__dict__


if __name__ == "main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.dict_)


try:
    print(my_square.size)
except AttributeError as e:
    print(e)


try:
    print(my_square._Square__size_)
except AttributeError as e:
    print(e)


my_square = Square(89)
print(type(my_square))
print(my_square.dict_)


my_square = Square(3)
print(type(my_square))
print(my_square.dict_)


try:
    print(my_square.size)
except AttributeError as e:
    print(e)


try:
    print(my_square._Square__size)
except AttributeError as e:
    print(e)
