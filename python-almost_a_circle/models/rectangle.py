#!/usr/bin/python3

"""Module:rectangle.py"""


from modles.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from base"""

def __intit__ (self, width, height, x=0, y=0, id=None):
    """Initialize Rectangle instance with width, height, x, y, and id"""
    
    
    if id is not None:
        self.id = id
    else:
        self.id = Rectangle.__nb_objects + 1
        Rectangle.__nb_objects += 1
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y


@property
def width(self):
    return self.__width


@width.setter
def width(self, value):
    self.__width =  value


@property
def height(self):
    return self.__height

@height.setter
def height(self, value):
    self.__height = value


@property
def x(self):
    return self.__x


@x.setter
def x(self, value):
    self.__x = value


@property
def y(self):
    return self.__y


@y.setter
def y(self, value):
    self.__y = value
