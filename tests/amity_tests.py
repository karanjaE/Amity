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

    def test_it_creates_livingspace(self):
        Amity.create_room('L', 'valhalla')
        room_names = [r.name for r in Amity.room_list]
        self.assertIn("VALHALLA", room_names)
        room1 = [room for room in Amity.room_list
                 if room.name == "VALHALLA"][0]
        self.assertEqual(room1.capacity, 4)

    def test_it_creates_office(self):
        Amity.create_room("O", "krypton")
        room_names = [r.name  for r in Amity.room_list]
        self.assertIn("KRYPTON", room_names)
        room = [room for room in Amity.room_list
                if room.name == "KRYPTON"][0]
        self.assertEqual(room.capacity, 6)

    def test_it_adds_person(self):
        Amity.add_person('jack', 'daniels', 'f', 'n')
        self.assertTrue(len(Amity.people_list))
        names = [p.name for p in Amity.people_list]
        self.assertIn("JACK DANIELS", names)

    def test_generate_random_room_none_with_no_rooms(self):
        random_lspace = Amity.generate_random_lspace()
        self.assertEqual(random_lspace, "None")
        random_office = Amity.generate_random_office()
        self.assertEqual(random_office, "None")

    @patch('amity.Office')
    def test_generate_random_office_with_rooms(self, mocked_office):
        mocked_office().name = "SHIRE"
        Amity.create_room("O", "Shire")
        random_office = Amity.generate_random_office()
        self.assertEqual(random_office.name, mocked_office().name)

    @patch('amity.LivingSpace')
    def test_generate_random_lspace_with_rooms(self, mocked_lspace):
        mocked_lspace().name = "OCCULUC"
        Amity.create_room("L", "OCCULUC")
        random_lspace = Amity.generate_random_lspace()
        self.assertEqual(random_lspace.name, mocked_lspace().name)

    def test_that_it_reallocates_person(self):
        # Amity.reallocate_person(id, )
        pass

    def test_it_prints_allocations(self):
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_prints_unallocated(self):
        Amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_loads_state(self):
        Amity.room_list = []
        Amity.people_list = []
        Amity.load_state("jjj")
        self.assertTrue(len(Amity.room_list))
        self.assertTrue(len(Amity.people_list))

    def test_it_saves_state(self):
        Amity.save_state('testdb')
        self.assertTrue(os.path.isfile('testdb.sqlite'))
        os.remove('testdb.sqlite')

if __name__ == '__main__':
    unittest.main()
