"""Herein are all tests that test the app's functions.
"""
import os

from mock import patch
from unittest import TestCase

from amity import *
# from db.migration import Base, Person, Room, DatabaseCreator
# from person.person import Fellow, Staff
# from room.room import LivingSpace, Office


class TestAmity(TestCase):
    """Test Amity functionality"""

    def setUp(self):
        pass

    def test_that_a_valid_room_type_is_passed(self):
        Amity.create_room("O", "Krypton")
        r = Amity.room_list[0]
        self.assertIn(r["type"], ["OFFICE", "LIVINGSPACE"])

    def test_that_a_room_name_has_already_been_taken(self):
        Amity.create_room('L', 'valhalla')

    def test_that_room_name_only_has_alphabets(self):
        pass

    def test_that_all_parameters_have_been_passed(self):
        pass

    def test_that_a_room_is_created(self):
        pass

    def it_generates_a_random_room(self):
        pass

    def test_that_add_person_receives_all_parameters(self):
        pass

    def test_that_first_name_and_last_name_only_have_alphabets(self):
        pass

    def test_that_a_valid_designation_is_passed(self):
        pass

    def test_that_staff_do_not_get_accomodation(self):
        pass

    def test_that_a_new_person_is_created(self):
        pass

    def test_new_person_is_added_to_people_list(self):
        pass

    def test_that_load_people_finds_a_file(self):
        pass

    def that_load_people_file_is_not_empty(self):
        pass

    def test_that_load_people_adds_the_people_to_people_list(self):
        pass

    def test_reallocate_person_creates_a_list_of_available_rooms(self):
        pass

    def test_reallocate_person_checks_that_requested_room_is_available(self):
        pass

    def test_reallocate_person_checks_that_person_id_entered_exists(self):
        pass

    def test_reallocate_person_checks_if_staff_wants_accomodation(self):
        pass

    def test_reallocate_person_checks_that_fellow_with_N_for_accomodation_wants_accomodation(self):
        pass

    def test_reallocate_person_checks_that_the_persons_office_is_updated(self):
        pass

    def test_reallocate_person_checks_that_a_persons_livingspace_is_updated(self):
        pass

    def test_reallocate_person_checks_thathat_the_newly_allocated_room_increases_occupants(self):
        pass

    def test_reallocate_person_checks_thareallocate_room_checks_that_the_previous_room_occupants_decrease_if_it_wasnt_none(self):
        pass

    def print_room_finds_a_room(self):
        pass

    def test_print_room_returns_empty_if_no_members_are_found(self):
        pass

    def test_print_room_returns_people_list(self):
        pass

    def test_print_unallocated_gets_inallocated_people(self):
        pass

    def test_print_allocations_returns_empty_if_room_has_no_occupants(self):
        pass

    def test_print_allocations_returns_all_members_of_all_rooms(self):
        pass

    def test_load_state(self):
        pass

    def test_save_state(self):
        pass
