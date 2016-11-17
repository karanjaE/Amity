import os

from unittest import TestCase

from room.room import LivingSpace, Office


class TestRoom(TestCase):

    def test_office(self):
        jade =  Office("JADE")
        self.assertEqual(jade.capacity, 6)
        self.assertEqual(jade.r_type, "OFFICE")

    def test_living_space(self):
        shire = LivingSpace("SHIRE")
        self.assertEqual(shire.capacity, 4)
        self.assertEqual(shire.r_type, "LIVINGSPACE")
