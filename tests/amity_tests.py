"""Herein are all tests that test the app's functions.
"""
import os

from unittest import TestCase

from amity import *
# from db.migration import Base, Person, Room, DatabaseCreator
# from person.person import Fellow, Staff
# from room.room import LivingSpace, Office


class TestAmity(TestCase):
    """Test Amity functionality"""

    def setUp(self):
        pass

    def test_that_it_creates_room(self):
        Amity.create_room('L', 'valhalla')
        Amity.create_room('O', 'jade')
        Amity.create_room('L', 'krypton')
        rooms = [r["name"] for r in Amity.room_list]
        self.assertIn("VALHALLA", rooms)
        res = "Dang! Name already taken. Enter another"
        self.assertEqual(Amity.create_room('L','valhalla'), None, msg=res)
        room1 = [room for room in Amity.room_list if room["name"] == "VALHALLA"]
        self.assertEqual(room1[0]["capacity"], 6)
        room2 = [room for room in Amity.room_list]

    def test_it_adds_person(self):
        Amity.add_person('Jonny', 'Walker', 'f', 'y')
        Amity.add_person('jack', 'daniels', 'f', 'n')
        Amity.add_person('the', 'rock', 's')
        Amity.add_person('stone','cold','s','n')
        self.assertTrue(len(Amity.people_list))
        fnames = [p["first_name"] for p in Amity.people_list]
        self.assertIn("JACK", fnames)

    def test_that_it_reallocates_person(self):
        Amity.create_room('L', 'shire')
        Amity.reallocate_person(1, 'l', 'shire')
        r = Amity.people_list[0]["livingspace"]
        self.assertEqual(r, "SHIRE")

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
