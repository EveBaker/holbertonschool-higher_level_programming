#!/usr/bin/python3
""" This module is a unittest for the Base class """

import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class for Base class """

    def setUp(self):
        """ Reset the __nb_objects counter and set up the test """
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

        Base._Base__nb_objects = 0

        self.base = Base()

    def tearDown(self):
        """ Clean up after the test """
        print("Base tearDown")

        sys.stdout = sys.__stdout__

        del self.base
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_print(self):
        """ Test print method """
        print("Hello, world!")
        self.assertEqual(self.capture_output.getvalue(), "Hello, world!\n")
        print("Hello, world!", file=sys.__stdout__)

    def test_id(self):
        """ Test id assignment and if it increments correctly """
        self.assertEqual(self.base.id, 1)
        base2 = Base(50)
        self.assertEqual(base2.id, 50)
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_too_many_args(self):
        """ Test too many args to init """
        with self.assertRaises(TypeError):
            Base(1, 1, 1, 1, 1, 1, 1)

    def test_to_json_string(self):
        """ Test to_json_string method """
        # Test empty list
        self.assertEqual(Base.to_json_string([]), "[]")
        # Test None
        self.assertEqual(Base.to_json_string(None), "[]")
        # Test normal list
        list_directories = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        ]
        expected_json = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        self.assertEqual(Base.to_json_string(list_directories), expected_json)

    def test_from_json_string(self):
        """ Test from_json_string method """
        # Test empty string
        self.assertEqual(Base.from_json_string(""), [])
        # Test empty list
        self.assertEqual(Base.from_json_string("[]"), [])
        # Test None
        self.assertEqual(Base.from_json_string(None), [])
        # Test normal list
        json_string = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        expected_list = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)
        # Test invalid json string
        with self.assertRaises(ValueError):
            Base.from_json_string("invalid")

    def test_save_to_file(self):
        """ Test save_to_file method """
        # Test None
        Base.save_to_file(None)
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")
        # Test empty list
        Base.save_to_file([])
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
