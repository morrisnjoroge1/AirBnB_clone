#!/usr/bin/python3
"""
testing for the file storage
the tests are in the methods: all, new, save, reload
"""
import json
import os
import unittest
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_filestorage(unittest.TestCase):
    """testing filestorage classes"""

    def test_instances_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instances_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_fileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

class Test_filestorage_methods(unittest.TestCase):
    """testing all the methods in the filestorage"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_dict(self):
        """test if all return dictionary"""
        obj = storage.all()
        self.assertEqual(type(obj), dict)

if __name__ == "__main__":
    unittest.main()
