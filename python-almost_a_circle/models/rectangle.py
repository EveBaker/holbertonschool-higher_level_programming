#!/usr/bin/python3

"""Rectangle class that inherits from Base."""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x (horizontal offset) of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x (horizontal offset) of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y (vertical offset) of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y (vertical offset) of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with '#' characters in stdout."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id":  self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """Assigns arguments or key/value arguments to the Rectangle attributes."""
        attributes = ["id", 'width', "height", 'x', "y"]
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
