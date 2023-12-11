#!/usr/bin/python3
"""Unit tests for place class"""

import unittest
import models
from models.place import Place
from datetime import datetime
from time import sleep
import os


class Test_Review(unittest.TestCase):
    """Test casess for Place class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.place = Place()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        self.place = None

    def test_init_with_arguments(self):
        """Test initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.place = Place(**data)

        # Verify that the attributes are set correctly
        self.assertEqual(self.place.id, '123')
        self.assertEqual(self.place.created_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.place.updated_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.place.name, 'Test')

    def test_init_without_arguments(self):
        """Test initialization without arguments"""
        self.place = Place()

        # Verify that the attributes are set correctly
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)
        self.assertEqual(self.place.created_at, self.place.updated_at)

    def test_unused_args(self):
        """Testing unused arguments during initialization"""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_with_keyword_arguments(self):
        """Testing with keyword arguments"""
        date = datetime.now()
        iso_format = date.isoformat()
        pl = Place(id="123", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(pl.id, "123")
        self.assertEqual(pl.created_at, date)
        self.assertEqual(pl.updated_at, date)


    def test_kwargs_None(self):
        """Verify behavior when kwargs are set to None"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_initialization_with_args_and_kwargs(self):
        """Test initialization with both positional arguments (args) and keyword arguments (kwargs)"""
        current_date = datetime.now()
        iso_formatted_date = current_date.isoformat()
        place_instance = Place(id="123", created_at=iso_formatted_date, updated_at=iso_formatted_date)
        self.assertEqual(place_instance.id, "123")
        self.assertEqual(place_instance.created_at, current_date)
        self.assertEqual(place_instance.updated_at, current_date)

    def test_attributes_initialization(self):
        """Verify attribute initialization"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))

    def test_id_is_str(self):
        """Verify that the 'id' attribute has the correct data type"""
        self.assertEqual(str, type(Place().id))

    def test_id_is_unique(self):
        """Check if generated ids are unique"""
        instance1 = Place()
        instance2 = Place()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_data_type(self):
        """Verify that the 'created_at' attribute is a datetime object"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_created_at_timestamp_difference(self):
        """Check if the timestamps are different"""
        instance1 = Place()
        sleep(0.05)
        instance2 = Place()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_updated_at_data_type(self):
        """Verify that the 'updated_at' attribute is a datetime object"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_updated_at_timestamp_difference(self):
        """Check if the timestamps are different"""
        instance1 = Place()
        sleep(0.05)
        instance2 = Place()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_instance_storage_and_retrieval(self):
        """Verify if storage and retrieval were successful"""
        self.assertIn(Place(), models.storage.all().values())

    def test_string_representation_difference(self):
        """Verify the difference in string representation"""
        instance1 = Place()
        instance2 = Place()
        self.assertNotEqual(str(instance1), str(instance2))


    def test_string_representation_method(self):
        """Verify the string representation method"""
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("id", place_str)
        self.assertIn("created_at", place_str)
        self.assertIn("updated_at", place_str)

    def test_save_effectiveness_timestamp_updates(self):
        """Verify the effectiveness of timestamp updates in the save() method"""
        place_instance = Place()
        sleep(0.1)
        original_update = place_instance.updated_at
        place_instance.save()
        self.assertLess(original_update, place_instance.updated_at)

    def test_two_saves_difference_in_timestamp_updates(self):
        """Verify the effectiveness of different timestamps updates with two saves"""
        place_instance = Place()
        sleep(0.1)
        update1 = place_instance.updated_at
        place_instance.save()
        update2 = place_instance.updated_at
        self.assertLess(update1, update2)
        sleep(0.1)
        place_instance.save()
        self.assertLess(update2, place_instance.updated_at)

    def test_save_updates_file_correctly(self):
        """Verify that updates are correctly updated and stored in the file"""
        place_instance = Place()
        place_instance.save()
        place_id = "Place." + place_instance.id
        with open("file.json", "r") as file:
            self.assertIn(place_id, file.read())

    def test_save_method(self):
        """Verify the save() method"""
        original_updated_at = self.place.updated_at
        self.place.save()
        updated_at_after_save = self.place.updated_at
        self.assertNotEqual(original_updated_at, updated_at_after_save)

    def test_to_dict_expected_output(self):
        """Verify the expected output of the to_dict() method"""
        expected_dict = {
            'id': self.place.id,
            'created_at': self.place.created_at.isoformat(),
            'updated_at': self.place.updated_at.isoformat(),
            '__class__': 'Place'
        }
        self.assertEqual(self.place.to_dict(), expected_dict)

    def test_to_dict_returns_dictionary(self):
        """Verify that the to_dict() method returns a dictionary"""
        place_instance = Place()
        self.assertTrue(dict, type(place_instance.to_dict()))

    def test_different_to_dict_for_diff_instances(self):
        """Verify that the class produces two different dictionaries for different instances"""
        place_instance1 = Place()
        sleep(0.05)
        place_instance2 = Place()
        self.assertNotEqual(place_instance1.to_dict(), place_instance2.to_dict())

    def test_to_dict_has_correct_keys(self):
        """Verify that the dictionary contains the correct keys"""
        place_instance = Place()
        self.assertIn("id", place_instance.to_dict())
        self.assertIn("__class__", place_instance.to_dict())
        self.assertIn("created_at", place_instance.to_dict())
        self.assertIn("updated_at", place_instance.to_dict())

    def test_to_dict_created_at_format(self):
        """Verify the ISO formatted string of the 'created_at' attribute"""
        place_dict = self.place.to_dict()
        created_at = place_dict["created_at"]
        self.assertEqual(created_at, self.place.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """Verify the ISO formatted string of the 'updated_at' attribute"""
        place_dict = self.place.to_dict()
        updated_at = place_dict["updated_at"]
        self.assertEqual(updated_at, self.place.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
