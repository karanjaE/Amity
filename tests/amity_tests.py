"""Herein are all tests that test the app's functions.
"""
import os

from mock import patch
from unittest import TestCase

from amity import Amity


class TestAmity(TestCase):
    """Test Amity functionality"""
    def test_create_room(self):
        """Checks that rooms are created"""
        self.assertEqual(type(Amity.people_list), list)
        
