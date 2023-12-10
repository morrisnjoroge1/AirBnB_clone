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
                'created_at': datetime(2023, 10, 15, 12, 0, 0),
                "updated_at": datetime(2023, 10, 15, 12, 1, 0),
                "name": "Test",
        }

        base_model = BaseModel(**arg)

        #check attributes are set correctly

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at,
                datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(base_model.updated_at,
                datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(base_model.name, 'Test')


if __name__ == "__main__":
    unittest.main()
