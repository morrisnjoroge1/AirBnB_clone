#!/usr/bin/python3
"""Unit tests for review class"""

import unittest
import models
from models.review import Review
from datetime import datetime
from time import sleep
import os


class Test_Review(unittest.TestCase):
    """Test casess for Review class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.review = Review()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        self.review = None

    def test_init_with_arguments(self):
        """Verify initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.review = Review(**data)

        # Check that the attributes are set correctly
        self.assertEqual(self.review.id, '123')
        self.assertEqual(self.review.created_at,
                        datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.review.updated_at,
                        datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.review.name, 'Test')

    def test_init_without_arguments(self):
        """Verify initialization without arguments"""
        self.review = Review()

        # Check that the attributes are set correctly
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)
        self.assertEqual(self.review.created_at, self.review.updated_at)

    def test_args_unused(self):
        """Verify unused args"""
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_with_kwargs(self):
        """Verify initialization with kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        rv = Review(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(rv.id, "123")
        self.assertEqual(rv.created_at, date)
        self.assertEqual(rv.updated_at, date)

    
    def test_kwargs_None(self):
        """Verify handling of kwargs set to None"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        """Verify initialization with both args and kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        rv = Review(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(rv.id, "123")
        self.assertEqual(rv.created_at, date)
        self.assertEqual(rv.updated_at, date)

    def test_attributes_initialization(self):
        """Verify attribute initialization"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_id_is_str(self):
        """Check if id is of type str"""
        self.assertEqual(str, type(Review().id))

    def test_id_is_unique(self):
        """Check if generated ids are unique"""
        user1 = Review()
        user2 = Review()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_datetime(self):
        """Check if the 'created_at' attribute is a datetime object"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_different_timestamps_for_updated_at(self):
        """Ensures that timestamps are different"""
        instance1 = Review()
        sleep(0.05)
        instance2 = Review()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_successful_instance_storage_and_retrieval(self):
        """Verifies successful storage and retrieval of instances"""
        self.assertIn(Review(), models.storage.all().values())

    def test_string_representation_difference(self):
        """Checks for differences in string representations"""
        review_instance1 = Review()
        review_instance2 = Review()
        self.assertNotEqual(review_instance1.__str__(), review_instance2.__str__())


    def test_string_representation_method(self):
        """Verifies the correctness of the str() method"""
        review_str = str(self.review)
        self.assertIn("[Review]", review_str)
        self.assertIn("id", review_str)
        self.assertIn("created_at", review_str)
        self.assertIn("updated_at", review_str)

    def test_save_effectiveness(self):
        """Checks the effectiveness of timestamp updates during save"""
        review_instance = Review()
        sleep(0.1)
        initial_update = review_instance.updated_at
        review_instance.save()
        self.assertLess(initial_update, review_instance.updated_at)

    def test_two_saves_effectiveness(self):
        """Checks the effectiveness of different timestamp updates during two saves"""
        review_instance = Review()
        sleep(0.1)
        initial_update = review_instance.updated_at
        review_instance.save()
        second_update = review_instance.updated_at
        self.assertLess(initial_update, second_update)
        sleep(0.1)
        review_instance.save()
        self.assertLess(second_update, review_instance.updated_at)

    def test_save_updates_file_correctly(self):
        """Verifies that updates are correctly stored and updated in the file"""
        review_instance = Review()
        review_instance.save()
        review_id = "Review." + review_instance.id
        with open("file.json", "r") as file:
            self.assertIn(review_id, file.read())

