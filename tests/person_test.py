import os

from unittest import TestCase

from person.person import Fellow, Staff


class TestPerson(TestCase):

    def test_fellow(self):
        jj = Fellow(1, "Nat", "Ross", "F")
        self.assertEqual(jj.designation, "FELLOW")

    def test_staff(self):
        jk = Staff(1, "Jon", "Jon", "S")
        self.assertEqual(jk.designation, "STAFF")
