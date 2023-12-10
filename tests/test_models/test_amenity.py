#!/usr/bin/python3
"""testing the amenity class"""

import unittest
from models.amenity import Amenity
import models
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    """class body"""
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(str(type(amenity)))

    def test_amenity_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        x = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(x, key))
            self.assertEqual(type(getattr(x, key, None)), value)

    def test_attributes_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertEqual(amenity.created_at, amenity.updated_at)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
