#!/usr/bin/python3
"""

Defines unittests for models/base_model.py.

"""

import unittest
import models
import os
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
                'id': str(uuid.uuid4()),
                'created_at': datetime(2023, 10, 15, 12, 00, 00),
                "updated_at": datetime(2023, 10, 15, 12, 01, 00),
                "updated_at": datetime(2023, 10, 15, 12, 01, 00),
                "name": "Test",
        }

        base_model = BaseModel(**arg)

        #check attributes are set correctly

        self.assertEqual(base_model.id, args['id'])
        self.assertEqual(base_model.created_at, args['created_at'])
        self.assertEqual(base_model.updated_at, args['updated_at'])
        self.assertEqual(base_model.name, args['name'])


if __name__ == "__main__":
    unittest.main()
