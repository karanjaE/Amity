import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from db.migration import Base, Person, Room, DatabaseCreator
from person.person import Fellow, Staff
from room.room import LivingSpace, Office


class Amity:
    people_list = []
    room_list = []

    @staticmethod
    def create_room(room_name, room_type):
        """Creates an empty room of the specified type."""
        if room_type.upper() not in ["L", "O"]:
            print("Dang!: Invalid room type entered. Use either O or L")
        elif not room_type or not room_name:
            print("Make sure you enter a room name and room type.")
        elif not room_name.isalpha():
            print("Room name can only contain alphabets. Try again")
        elif room_name.upper() in [room["name"] for room in Amity.room_list]:
            print("Dang! Name already taken. Enter another")
        else:
            office = Office()
            l_space = LivingSpace()
            new_room = {}
            new_room["name"] = room_name.upper()
            new_room["occupants"] = 0
            if room_type.upper() in ['O', "OFFICE"]:
                new_room["type"] = office.r_type
                new_room["capacity"] = office.capacity
            elif room_type.upper() in ["L", "LIVINGSPACE"]:
                new_room["type"] = l_space.r_type
                new_room["capacity"] = l_space.capacity

            Amity.room_list.append(new_room)

    @staticmethod
    def generate_random_room(room_type):
        """Generates a random room of the given type."""
        if room_type.upper() == 'L':
            # print(Amity.room_list)
            rooms = [room["name"] for room in Amity.room_list
                     if room["type"] == "LIVINGSPACE"]
        elif room_type.upper() == "O":
            rooms = [room["name"] for room in Amity.room_list
                     if room["type"] == "OFFICE"]

        if len(rooms) > 0:
            return random.choice(rooms)
        else:
            return "None"

    @staticmethod
    def add_person(first_name, last_name, designation, needs_accomodation="N"):
        """Adds a new person and allocates a random room to them."""
        if not first_name.isalpha() or not last_name.isalpha():
            print("Error! Names can only have alphabets!")
        elif designation.upper() not in ['S', 'STAFF', 'F', 'FELLOW']:
            print("Invalid designation. Enter F or FELLOW or S or STAFF")
        elif needs_accomodation.upper() not in ["Y", "YES", "N", "NO"]:
            print("Invalid option. Enter a valid accomodation request option!")
        elif (designation.upper() in ["S", "STAFF"] and
              needs_accomodation.upper() in ["Y", "YES"]):
            print("Staff members cannot get accomodation!")
        else:
            allocated_office = Amity.generate_random_room("O")
            allocated_lspace = Amity.generate_random_room("L")
            new_person = {}
            new_person["first_name"] = first_name
            new_person["last_name"] = last_name
            new_person["accomodated"] = needs_accomodation
            new_person["office"] = allocated_office
            if designation.upper() in ["F", "FELLOW"]:
                new_person["designation"] = Fellow.designation
                


    @staticmethod
    def load_people(filename):
        """Loads people from a file.txt into the app and creates them"""
        with open(filename, 'r') as people_file:
            for person_dets in people_file:
                details = person_dets.rstrip().split()
                accomodate = details[3] if len(details) == 4 else "N"
                Amity.add_person(details[0], details[1], details[2],
                                 accomodate)

    @staticmethod
    def reallocate_person(full_name, room_type, new_room):
        """Moves a person to another room"""
        pass

    @staticmethod
    def remove_person(first_name, last_name):
        """Removes a person from the system"""
        pass

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        all_rooms = [room.r_name for room in Amity.room_list]
        room_members = []
        if room_name not in all_rooms:
            print("Room does not exist")
        else:
            for person in Amity.people_list:
                if type(person.office) == object or type(person.living_space) == object:
                    if person.office == room_name or person.living_space == room_name:
                        full_name = person.first_name + " " + person.last_name
                        room_members.append(full_name)
            print(room_members if len(room_members) > 0 else "Room is empty")


    @staticmethod
    def print_allocations():
        """Prints all the people that have rooms and arranges by room"""
        pass

    @staticmethod
    def print_unallocated():
        """Prints all the people who don't have rooms"""
        unallocated_people = []

        print("People with no offices:")
    @staticmethod
    def load_state():
        """Loads data from a DB file into the app."""
        pass

    @staticmethod
    def save_state(db_name=None):
        """Persists data saved in the app to a db"""
        if not db_name:
            db = DatabaseCreator()
        else:
            db = DatabaseCreator(db_name)
        Base.metadata.bind = db.engine
        s = db.session()
        for room in Amity.rooms_list:
            rooms_to_save = Room(
                name=room.r_name,
                r_type=room.r_type,
                capacity=room.capacity,
                members=room.members
            )
        for person in Amity.people_list:
            people_to_save = Person(
                first_name=person.first_name,
                last_name=person.last_name,
                accomodated=person.accomodate_opt,
                designation=person.designation,
                office=person.office,
                l_space=person.living_space
            )
