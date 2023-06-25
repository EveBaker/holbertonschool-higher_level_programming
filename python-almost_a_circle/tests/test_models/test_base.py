import json
import unittest
from base import Base


class TestBase(unittest.TestCase):

    def test_assign_auto_id(self):
        # Test that Base assigns automatic IDs
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_assign_auto_id_plus_one(self):
        # Test that Base assigns automatic IDs incremented from the previous ID
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)
        self.assertEqual(obj3.id, 5)

    def test_assign_passed_id(self):
        # Test that Base assigns the ID passed in the constructor
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_none(self):
        # Test Base.to_json_string with None input
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        # Test Base.to_json_string with an empty list
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_single_dict(self):
        # Test Base.to_json_string with a list containing a single dictionary
        list_dicts = [{"id": 12}]
        expected_json = json.dumps(list_dicts)
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_return_type(self):
        # Test that Base.to_json_string returns a string
        list_dicts = [{"id": 12}]
        json_string = Base.to_json_string(list_dicts)
        self.assertIsInstance(json_string, str)

    def test_from_json_string_none(self):
        # Test Base.from_json_string with None input
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        # Test Base.from_json_string with an empty string
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_single_dict(self):
        # Test Base.from_json_string with a JSON string containing a single dictionary
        json_string = '[{ "id": 89 }]'
        expected_list = [{"id": 89}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    def test_from_json_string_return_type(self):
        # Test that Base.from_json_string returns a list
        json_string = '[{ "id": 89 }]'
        result_list = Base.from_json_string(json_string)
        self.assertIsInstance(result_list, list)


if __name__ == '__main__':
    unittest.main()
    