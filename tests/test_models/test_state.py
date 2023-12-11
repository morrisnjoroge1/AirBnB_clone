#!/usr/bin/python3
"""Unit tests for state class"""

import unittest
import models
from models.state import State
from datetime import datetime
from time import sleep
import os


class Test_State(unittest.TestCase):
    """Test casess for State class"""

    def setUp(self):
        """Set up the env before each test case"""
        self.state = State()

    def tearDown(self):
        """Clean up the test env after each test case if needed"""
        self.state = None


    def test_init_with_arguments(self):
        """Verify initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.state = State(**data)

        # Ensure attributes are set correctly
        self.assertEqual(self.state.id, '123')
        self.assertEqual(self.state.created_at,
                        datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.state.updated_at,
                    datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.state.name, 'Test')

    def test_init_without_arguments(self):
        """Verify initialization without arguments"""
        self.state = State()

        # Ensure attributes are set correctly
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)
        self.assertEqual(self.state.created_at, self.state.updated_at)

    def test_args(self):
        """Verify handling of unused args"""
        st = State(None)
        self.assertNotIn(None, st.__dict__.values())
    
    def test_with_kwargs(self):
    """Verify handling of kwargs"""
    date = datetime.now()
    tform = date.isoformat()
    st = State(id="123", created_at=tform, updated_at=tform)
    self.assertEqual(st.id, "123")
    self.assertEqual(st.created_at, date)
    self.assertEqual(st.updated_at, date)

    def test_kwargs_None(self):
        """Verify handling of kwargs with None values"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        """Verify handling of both args and kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        st = State(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(st.id, "123")
        self.assertEqual(st.created_at, date)
        self.assertEqual(st.updated_at, date)

    def test_attribute_initialization(self):
        """Verify attribute initialization"""
        self.assertEqual(self.state.name, "")
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_id_is_str(self):
        """Verify id data type"""
        self.assertEqual(str, type(State().id))

    def test_id_is_unique(self):
        """Verify uniqueness of generated ids"""
        user1 = State()
        user2 = State()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_datetime(self):
        """Verify if the attribute is a datetime object"""
        self.assertEqual(datetime, type(State().created_at))

