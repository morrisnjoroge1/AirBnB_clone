#!/usr/bin/python3
"""Unit tests for user class"""

import unittest
import models
from models.user import User
from datetime import datetime
from time import sleep
import os


class Test_User(unittest.TestCase):
    """Test casess for User class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.user = User()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        del self.user


    def test_instance_creation(self):
        """Ensure that an instance is created correctly"""
        self.assertIsInstance(self.user, User)

    def test_init_with_arguments(self):
        """Verify initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.user = User(**data)

        # Confirm that the attributes are set correctly
        self.assertEqual(self.user.id, '123')
        self.assertEqual(self.user.created_at,
                        datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.user.updated_at,
                        datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.user.name, 'Test')


    def test_init_without_arguments(self):
        """Verify initialization without arguments"""
        self.user = User()

        # Confirm that the attributes are set correctly
 
        self.assertIsNotNone(self.user.id)
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_args(self):
        """Check unused args"""
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_with_kwargs(self):
        """Verify initialization with kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        usr = User(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(usr.id, "123")
        self.assertEqual(usr.created_at, date)
        self.assertEqual(usr.updated_at, date)


    def test_kwargs_none(self):
        """Test passing None for all kwargs."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        """Test passing both args and kwargs."""
        date_now = datetime.now()
        iso_format = date_now.isoformat()
        user = User(id="123", created_at=iso_format, updated_at=iso_format)
        self.assertEqual(user.id, "123")
        self.assertEqual(user.created_at, date_now)
        self.assertEqual(user.updated_at, date_now)

    def test_user_attributes(self):
        """Test presence of specific attributes in User class."""
        expected_attributes = ["email", "password", "first_name", "last_name"]
        for attribute in expected_attributes:
            self.assertTrue(hasattr(self.user, attribute))

