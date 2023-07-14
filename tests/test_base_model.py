#!/usr/bin/python3
import os
import sys
import unittest
from datetime import datetime

current_dir = os.getcwd()

root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_object_creation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.to_dict()}"
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        my_model = BaseModel()
        my_model.save()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.name = "Test Model"
        my_model.my_number = 42
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
        self.assertEqual(my_model_dict['name'], "Test Model")
        self.assertEqual(my_model_dict['my_number'], 42)

    def test_attribute_arguement(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        self.assertEqual(my_model.name, "Test Model")
        self.assertEqual(my_model.my_number, 42)

    def test_attribute_modification(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        my_model.name = "Updated Model"
        my_model.my_number = 24
        self.assertEqual(my_model.name, "Updated Model")
        self.assertEqual(my_model.my_number, 24)

    def test_attribute_deletion(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        del my_model.name
        self.assertFalse(hasattr(my_model, "name"))

    def test_serialization_deserialization(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42

        serialized_data = my_model.to_dict()
        deserialized_model = BaseModel(**serialized_data)

        self.assertEqual(my_model.id, deserialized_model.id)
        self.assertEqual(my_model.name, deserialized_model.name)
        self.assertEqual(my_model.my_number, deserialized_model.my_number)


if __name__ == '__main__':
    unittest.main
