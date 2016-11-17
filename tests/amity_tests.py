"""Herein are all tests that test the app's functions.
"""
import os

from unittest import TestCase
from mock import patch

from amity import *
# from db.migration import Base, Person, Room, DatabaseCreator
# from person.person import Fellow, Staff
# from room.room import LivingSpace, Office


class TestAmity(TestCase):
    """Test Amity functionality"""
    
    def test_it_creates_office(self):
        Amity.room_list = []
        Amity.create_room("o", "lime")
        self.assertNotEqual(len(Amity.room_list), 0)
        self.assertIn("LIME", Amity.office_allocations.keys())
        Amity.room_list = []

    def test_it_creates_livingspace(self):
        Amity.room_list = []
        Amity.create_room("l", "lime")
        self.assertNotEqual(len(Amity.room_list), 0)
        self.assertIn("LIME", Amity.lspace_allocations.keys())
        Amity.room_list = []

    def test_it_adds_person(self):
        Amity.people_list = []
        Amity.add_person("eddy", "karanja", "F", "Y")
        Amity.add_person("jim", "jim", "S")
        self.assertNotEqual(len(Amity.people_list), 0)

    def test_it_prints_allocations(self):
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_prints_unallocated(self):
        Amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_saves_state(self):
        Amity.save_state('testdb')
        self.assertTrue(os.path.isfile('testdb.sqlite'))
        os.remove('testdb.sqlite')


if __name__ == '__main__':
    unittest.main()
