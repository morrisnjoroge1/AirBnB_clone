#!/usr/bin/python3
"""

Defines unittests for models/base_model.py.

"""

import unittest
import models
import os
from uuid import uuid4
from  datetime import datetime
from models.base_model import BaseModel
from time import sleep


class Test_BaseModel(unittest.TestCase):
    """testing case for BasesModel class."""

    def setUp(self):
        """sets up environment for each test case."""
        self.model = BaseModel()

    def tearDown(self):
        """cleans the environment after each test if needed"""
        pass

    def test_init_with_arguments(self):
        """test initialization with argumentas(kwargs)"""

        args ={
                'id': '123',
                'created_at': '2023-12-01T00:00:00',
                "updated_at": '2023-12-01T00:00:00',
                "name": "Test",
        }

        base_model = BaseModel(**args)

        #check attributes are set correctly

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at,
                datetime.fromisoformat('2023-12-01T00:00:00'))
        self.assertEqual(base_model.updated_at,
                datetime.fromisoformat('2023-12-01T00:00:00'))
        self.assertEqual(base_model.name, 'Test')


    def test_init_without_arguments(self):
        """test without arguments"""
        base_model = BaseModel()

        #check attributes are set correctly
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_args(self):
        """args that are used"""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_init_with_kwargs(self):
        """Test initialization with kwargs."""
        date = datetime.now()
        tform = date.isoformat()
        bm = BaseModel(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, date)
        self.assertEqual(bm.updated_at, date)

    def test_init_without_kwargs(self):
        """test initialization with kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save(self):
        """effectiveness of timestamps updates"""
        bm = BaseModel()
        sleep(0.1)
        update = bm.updated_at
        bm.save()
        self.assertLess(update, bm.updated_at)


    def test_generated_ids_are_unique(self):
        """Verifies that the generated 'id' values are unique."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_is_datetime_object(self):
        """Verifies that the 'created_at' attribute is of type datetime."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_created_at_timestamp_difference(self):
        """Verifies that the timestamps are different."""
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_is_datetime_object(self):
        """Verifies that the 'updated_at' attribute is of type datetime."""
        self.assertEqual(datetime, type(BaseModel().updated_at))


    def test_updated_at_timestamp_difference(self):
        """Verifies that the timestamps are different."""
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertLess(instance1.updated_at, instance2.updated_at)


    def test_string_representation(self):
        """Verifies that the string representations are different."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(str(instance1), str(instance2))

    def test_multiple_saves_effectiveness(self):
        """Verifies the effectiveness of updating timestamps with multiple saves."""
        instance = BaseModel()
        sleep(0.1)
        initial_update = instance.updated_at
        instance.save()
        subsequent_update = instance.updated_at
        self.assertLess(initial_update, subsequent_update)
        sleep(0.1)
        instance.save()
        self.assertLess(subsequent_update, instance.updated_at)

    def test_save_updates_file_correctly(self):
        """Verifies that updates are correctly stored and reflected in the file."""
        instance = BaseModel()
        instance.save()
        instance_id = "BaseModel." + instance.id
        with open("file.json", "r") as file:
            self.assertIn(instance_id, file.read())


    def test_to_dict_expected_output(self):
        """Verifies that the to_dict method produces the expected output."""
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_to_dict_returns_dictionary(self):
        """Ensures that the class returns a dictionary."""
        instance = BaseModel()
        self.assertTrue(dict, type(instance.to_dict()))

    def test_unique_to_dict_for_different_instances(self):
        """Verifies that the class generates distinct dictionaries for different instances."""
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertNotEqual(instance1.to_dict(), instance2.to_dict())

    def test_to_dict_contains_expected_keys(self):
        """Ensures that the dictionary contains the correct keys."""
        instance = BaseModel()
        self.assertIn("id", instance.to_dict())
        self.assertIn("__class__", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())


    def test_to_dict_created_at_iso_format(self):
        """Verifies that the 'created_at' value is in ISO format."""
        instance_dict = self.base_model.to_dict()
        created_at_value = instance_dict["created_at"]
        self.assertEqual(created_at_value, self.base_model.created_at.isoformat())

    def test_to_dict_updated_at_iso_format(self):
        """Verifies that the 'updated_at' value is in ISO format."""
        instance_dict = self.base_model.to_dict()
        updated_at_value = instance_dict["updated_at"]
        self.assertEqual(updated_at_value, self.base_model.updated_at.isoformat())




if __name__ == "__main__":
    unittest.main()
