"""This module defines the base properties of people classes. Amity will
inheri from it while performing the apps main functionalities
"""


class Person(object):
    def __init__(self, first_name, last_name, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.accomodate_opt = None
        self.living_space = None
        self.office = None


class Fellow(Person):
    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(first_name, last_name,
                                     designation="FELLOW")


class Staff(Person):
    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name, designation="STAFF")
