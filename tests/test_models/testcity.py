#!/usr/bin/python3
"""Unit tests for city class"""

import unittest
import models
from models.city import City
from datetime import datetime
from time import sleep
import os


class Test_City(unittest.TestCase):
    """Test casess for City class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.city = City()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        self.city = None

    def test_init_with_arguments(self):
        """Test initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.city = City(**data)

        # Verify that the attributes are set correctly
        self.assertEqual(self.city.id, '123')
        self.assertEqual(self.city.created_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.city.updated_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.city.name, 'Test')


    def test_initialization_without_arguments(self):
        """Verify initialization without arguments"""
        self.city = City()

        # Ensure that the attributes are appropriately set
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)
        self.assertEqual(self.city.created_at, self.city.updated_at)


    def test_unused_args(self):
        """Check for unused arguments"""
        city_instance = City(None)
        self.assertNotIn(None, city_instance.__dict__.values())


    def test_initialization_with_kwargs(self):
        """Test initialization with keyword arguments (kwargs)"""
        current_date = datetime.now()
        iso_formatted_date = current_date.isoformat()
        city_instance = City(id="123", created_at=iso_formatted_date, updated_at=iso_formatted_date)
        self.assertEqual(city_instance.id, "123")
        self.assertEqual(city_instance.created_at, current_date)
        self.assertEqual(city_instance.updated_at, current_date)

    def test_kwargs_set_to_None(self):
        """Verify behavior when kwargs are set to None"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


    def test_initialization_with_args_and_kwargs(self):
        """Test initialization with both positional arguments (args) and keyword arguments (kwargs)"""
        current_date = datetime.now()
        iso_formatted_date = current_date.isoformat()
        city_instance = City(id="123", created_at=iso_formatted_date, updated_at=iso_formatted_date)
        self.assertEqual(city_instance.id, "123")
        self.assertEqual(city_instance.created_at, current_date)
        self.assertEqual(city_instance.updated_at, current_date)
    
    def test_attributes_initialization(self):
        """Verify attribute initialization"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_id_data_type(self):
        """Check the data type of the 'id' attribute"""
        self.assertEqual(str, type(City().id))

    def test_unique_generated_ids(self):
        """Check if generated ids are unique"""
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_data_type(self):
        """Verify that the 'created_at' attribute is a datetime object"""
        self.assertEqual(datetime, type(City().created_at))

    def test_created_at_timestamp_difference(self):
        """Check if the timestamps are different"""
        instance1 = City()
        sleep(0.05)
        instance2 = City()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_data_type(self):
        """Verify that the 'updated_at' attribute is a datetime object"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_updated_at_timestamp_difference(self):
        """Check if the timestamps are different"""
        instance1 = City()
        sleep(0.05)
        instance2 = City()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_instance_storage_and_retrieval(self):
        """Check if storage and retrieval were successful"""
        self.assertIn(City(), models.storage.all().values())


    def test_string_representation_difference(self):
        """Verify the difference in string representation"""
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(str(instance1), str(instance2))

    def test_str_method_contents(self):
        """Verify the contents of the string representation"""
        city_str = str(self.city)
        self.assertIn("[City]", city_str)
        self.assertIn("id", city_str)
        self.assertIn("created_at", city_str)
        self.assertIn("updated_at", city_str)

    def test_save_effectiveness(self):
        """Verify the effectiveness of timestamp updates with a single save"""
        city_instance = City()
        sleep(0.1)
        initial_update = city_instance.updated_at
        city_instance.save()
        self.assertLess(initial_update, city_instance.updated_at)

    def test_two_saves_effectiveness(self):
        """Verify the effectiveness of different timestamp updates with multiple saves"""
        city_instance = City()
        sleep(0.1)
        update1 = city_instance.updated_at
        city_instance.save()
        update2 = city_instance.updated_at
        self.assertLess(update1, update2)
        sleep(0.1)
        city_instance.save()
        self.assertLess(update2, city_instance.updated_at)


    def test_save_updates_file_correctly(self):
        """Verify that updates are correctly stored in the file"""
        city_instance = City()
        city_instance.save()
        city_id = "City." + city_instance.id
        with open("file.json", "r") as file:
            self.assertIn(city_id, file.read())

    def test_save_method_effectiveness(self):
        """Verify the effectiveness of the save method"""
        initial_updated_at = self.city.updated_at
        self.city.save()
        updated_at_after_save = self.city.updated_at
        self.assertNotEqual(initial_updated_at, updated_at_after_save)

    def test_to_dict_expected_output(self):
        """Verify the expected output of the to_dict method"""
        expected_dict = {
            'id': self.city.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            '__class__': 'City'
        }
        self.assertEqual(self.city.to_dict(), expected_dict)

    def test_to_dict_returns_dictionary(self):
        """Verify that the to_dict method returns a dictionary"""
        city_instance = City()
        self.assertTrue(dict, type(city_instance.to_dict()))

    def test_different_to_dict_for_diff_instances(self):
        """Verify that the class produces different dictionaries for different instances"""
        city_instance1 = City()
        sleep(0.05)
        city_instance2 = City()
        self.assertNotEqual(city_instance1.to_dict(), city_instance2.to_dict())


    def test_to_dict_has_correct_keys(self):
        """Verify that the dictionary contains the correct keys"""
        city_instance = City()
        self.assertIn("id", city_instance.to_dict())
        self.assertIn("__class__", city_instance.to_dict())
        self.assertIn("created_at", city_instance.to_dict())
        self.assertIn("updated_at", city_instance.to_dict())

    def test_to_dict_created_at_format(self):
        """Check the ISO formatted string of the 'created_at' attribute in the dictionary"""
        city_dict = self.city.to_dict()
        created_at_in_dict = city_dict["created_at"]
        self.assertEqual(created_at_in_dict, self.city.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """Check the ISO formatted string of the 'updated_at' attribute in the dictionary"""
        city_dict = self.city.to_dict()
        updated_at_in_dict = city_dict["updated_at"]
        self.assertEqual(updated_at_in_dict, self.city.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
