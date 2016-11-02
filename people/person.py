"""This module defines the base properties of people classes. Amity will inherit
from it while performing the apps main functionalities
"""
class Person(object):
    def __init__(self, designation=None, needs_acc="N"):
        self.designation = designation
        # self.office = office
        self.needs_acc = needs_acc

class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(designation="FELLOW")

class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(designation="STAFF")
