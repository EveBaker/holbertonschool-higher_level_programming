import json
from unittest import TestCase
from base import Base


class TestBase(TestCase):

    def test_to_json_string(self):
        # Test with empty list of dictionaries
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test with a list of dictionaries
        list_dicts = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
        expected_json = json.dumps(list_dicts)
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_from_json_string(self):
        # Test with empty JSON string
        self.assertEqual(Base.from_json_string(""), [])

        # Test with a JSON string
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_list = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_save_to_file(self):
        # Test with an empty list of objects
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test with a list of objects
        # Assume we have a class Rectangle with a to_dictionary() method
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def to_dictionary(self):
                return {"width": self.width, "height": self.height}

        rectangles = [Rectangle(2, 3), Rectangle(4, 5)]
        Base.save_to_file(rectangles)
        with open("Rectangle.json", "r") as file:
            expected_json = json.dumps([r.to_dictionary() for r in rectangles])
            self.assertEqual(file.read(), expected_json)

    def test_create(self):
        # Test creating an instance of Rectangle
        # Assume we have a class Rectangle with an update() method
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def update(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)

        # Create a dummy instance of Rectangle
        dummy = Base.create(width=2, height=3)
        self.assertIsInstance(dummy, Rectangle)
        self.assertEqual(dummy.width, 2)
        self.assertEqual(dummy.height, 3)

    def test_load_from_file(self):
        # Test loading instances from a JSON file
        # Assume we have a class Square with a create() method
        class Square:
            def __init__(self, side):
                self.side = side

            @classmethod
            def create(cls, **kwargs):
                instance = cls(0)  # Create a dummy instance
                instance.__dict__.update(kwargs)  # Update dummy instance with attributes
                return instance

        # Create a JSON file with instances of Square
        json_data = '[{"side": 2}, {"side": 4}, {"side": 6}]'
        with open("Square.json", "w") as file:
            file.write(json_data)

        # Load instances from the JSON file
        instances = Base.load_from_file()
        self.assertIsInstance(instances[0], Square)
        self.assertEqual(instances[0].side, 2)
        self.assertIsInstance(instances[1], Square)
        self.assertEqual(instances[1].side, 4)
        self.assertIsInstance(instances[2], Square)
        self.assertEqual(instances[2].side, 6)

    if __name__ == '__main__':
        unittest.main()