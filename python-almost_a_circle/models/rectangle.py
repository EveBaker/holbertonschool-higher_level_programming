#!/usr/bin/python3
class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class
        """
        if id is not None:
            self.id = id
        else:
            self.id = super().generate_id()

        self.width = width
        self.height = height
        self.x = x
        self.y = y
