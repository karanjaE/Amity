import os

from unittest import TestCase

from person.person import Fellow, Staff


class TestPerson(TestCase):

    def test_fellow(self):
        jj = Fellow("Nat", "Ross")
        self.assertEqual(jj.designation, "FELLOW")

    def test_staff(self):
        jk = Staff("Jon", "Jon")
        self.assertEqual(jk.designation, "STAFF")
