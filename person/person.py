"""This module defines the base properties of people classes. Amity will
inheri from it while performing the apps main functionalities
"""


class Person(object):
    def __init__(self, person_id, first_name, last_name, designation):
        self.id = person_id
        self.name = first_name + " " + last_name
        self.designation = designation


class Fellow(Person):
    def __init__(self, person_id, first_name, last_name, designation):
        super(Fellow, self).__init__(person_id, first_name, last_name,
                                     designation="FELLOW")


class Staff(Person):
    def __init__(self, person_id, first_name, last_name, designation):
        super(Staff, self).__init__(person_id, first_name, last_name,
                                    designation="STAFF")
