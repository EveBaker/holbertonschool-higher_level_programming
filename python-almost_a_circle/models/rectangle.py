"""
Rectangle Module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        """

        if id is not None:
            self.id = id
        else:
            self.id = Rectangle.get_next_id()

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def get_next_id():
        """
        Retrieves the next available ID for a Rectangle.
        """
        if Rectangle.__name__ == "Rectangle":
            return Base._Base__nb_objects + 1

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate of the rectangle.
        """
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a visual representation of the rectangle.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

