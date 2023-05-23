#!/usr/bin/python3
"""
Module: 2-rectangle
Rectangle class with width and height attributes
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialization method
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.perimeter()))
