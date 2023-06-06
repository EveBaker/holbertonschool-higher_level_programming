#!/usr/bin/python3
""" 
This module is a unittest for the Rectangle class 
"""

import unittest
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test class for Rectangle class 
    """
    def setUp(self):
        """
        Set up test method
        """
        print("Rectangle setUp")

        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

        self.rectangle = Rectangle(1, 1)

        # reset __nb_objects to 0 before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        """
        Tear down test method
        """
        print("Rectangle tearDown")

        sys.stdout = sys.__stdout__

        del self.rectangle
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """
        Test id assignment in the Rectangle class
        """
        print(f"Actual id: {self.rectangle.id}")
        self.assertEqual(self.rectangle.id, 1)
        rectangle2 = Rectangle(50, 50)
        print(f"Actual id: {rectangle2.id}")
        self.assertEqual(rectangle2.id, 1)
        rectangle3 = Rectangle(1, 1)
        print(f"Actual id: {rectangle3.id}")
        self.assertEqual(rectangle3.id, 2)

    def test_too_many_args(self):
        """
        Test too many args to init
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1, 1)

    def test_rectangle_creation(self):
        """
        Test Rectangle creation
        """
        # basic rectangle
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # rectangle with x
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

        # rectangle with y
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        # rectangle with id
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

        # rectangle with negative width
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)

        # rectangle with negative height
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)

        # rectangle with negative x
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)

        # rectangle with negative y
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)

        # rectangle with zero width
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)


    def test_save_to_file_normal_list(self):
        """
        Test if save_to_file method saves a list with a single
        Rectangle to file
        """
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_json = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
            self.assertEqual(content, expected_json)

    def test_load_from_file_file_not_exist(self):
        """
        Test load_from_file method when the file doesn't exist
        """
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_file_exists(self):
        """
        Test load_from_file method when the file exists
        """
        # Create a dummy file with sample JSON content
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]')

        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        r = rectangles[0]
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        # Clean up the dummy file
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
