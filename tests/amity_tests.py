"""Herein are all tests that test the app's functions.
"""
import os

from mock import patch
from unittest import TestCase

from app import Amity


class TestAmity(TestCase):

    def test_create_room(self):
        """Checks that a room is successfully created and added to the existing
        rooms_list
        """
        self.assertEqual(Amity.create_room('nam3', 'l'), msg=)

    def test_if_error_is_thrown_if_non_alphabet_is_passed_on_room_name(self):
        """Checks that all the characters in the room name is not a string
        and throws an error if it isn't
        """
        pass

    def test_if_invalid_room_type_is_passed(self):
        """Checks that the room_type passed is either 'O' ir 'L' and throws an
        error if a different type is passed
        """
        pass

    def test_if_room_name_is_blank(self):
        """Ensures room name is not blank"""
        pass

    def test_if_room_name_already_exists(self):
        """Checks if the room name exists and returns an error if it does"""
        pass

    def test_print_room(self):
        """Checks that the nethod prints the room passed"""
        pass

    def test_print_allocations(self):
        """Checks that the method prints allocations"""
        pass

    def test_add_person(self):
        """Tests that a person is added successfully"""
        pass

    def test_reallocate_person(self):
        """Tests that a person is reallocated successfully
        Checks that the new room has space"""
        pass

    def test_remove_person(self):
        """Tests that a person is sussesfully removed.."""
        pass

    def test_print_unallocated(self):
        """Tests that people with no allocations is output"""
        pass

    def test_load_people(self):
        """Tests that the method loads the txt file.
        Also checks that the file exists and is not empty"""
        pass

    def test_load_state(self):
        """checks that the db is valid and that it is deleted after loading
        """
        pass

    def test_save_state(self):
        """Tests that data is persisted to the SQLite db"""
        pass
