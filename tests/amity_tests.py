import sys
import unittest

sys.path.append("../../checkpoints/")

from Amity.amity import amity

class TestAmity(unittest.TestCase):
    def setUp(self):
        amity.Amity.create_room("Shu", "O")
        amity.Amity.create_room("Bay", "L")
        amity.Amity.add_person("Jim", "F")
        amity.Amity.add_person("Lee", "S")

    def test_create_room(self):
        """Tests if a new room is created.
        """
        self.assertIn("Shu", amity.Amity.rooms_list)

    def test_room_capacity(self):
        """Checks for room capacity. Offices have a capacity of 6 and living spaces
        have 4.
        """
        self.assertEqual(amity.Amity.rooms_list["Shu"]["Capacity"], 6)
        self.assertEqual(amity.Amity.rooms_list["Bay"]["Capacity"], 4)

    def test_if_room_has_space(self):
        """Return true is the number of members in a room is less than the
        calacity.
        """
        self.assertLess(len(amity.Amity.rooms_list["Shu"]["Occupants"]), 6)
        self.assertLess(len(amity.Amity.rooms_list["Bay"]["Occupants"]), 4)

    def test_add_person(self):
        self.assertIn("Lee", amity.Amity.people_list)

    def test_if_person_is_fellow_or_staff(self):
        self.assertEqual("FELLOW", amity.Amity.people_list["Jim"]["Designation"])
        self.assertEqual("STAFF", amity.Amity.people_list["Lee"]["Designation"])

    def test_allocates_office(self):
        self.assertNotEqual(amity.Amity.people_list["Lee"]["Office"], "None")

    def test_allocates_living_space(self):
        self.assertNotEqual(amity.Amity.people_list["Jim"]["L-Space"], "None")

    def test_reallocates_person(self):
        amity.Amity.reallocate_person("Jim", 'O', "Shu")
        self.assertEqual(amity.Amity.people_list["Jim"]["Office"], "Shu")

    def test_print_allocations(self):
        """Dicstring
        """
        pass

    def test_unallocated(self):
        pass

    def test_load_people(self):
        pass

    def test_load_state(self):
        pass

    def test_save_state(self):
        pass
