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
            rooms = [room["name"] for room in Amity.room_list
                     if room["type"] == "LIVINGSPACE"
                     and room["occupants"] < room["capacity"]]
        elif room_type.upper() == "O":
            rooms = [room["name"] for room in Amity.room_list
                     if room["type"] == "OFFICE"
                     and room["occupants"] < room["capacity"]]

        if len(rooms) > 0:
            return random.choice(rooms)
        else:
            return "None"

    @staticmethod
    def add_person(first_name, last_name, designation, needs_accomodation="NO"):
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
            new_person["first_name"] = first_name.upper()
            new_person["last_name"] = last_name.upper()
            new_person["office"] = allocated_office
            if designation.upper() in ["F", "FELLOW"] and \
            needs_accomodation.upper() in ["Y", "YES"]:
                new_person["accomodated"] = "YES"
                new_person["livingspace"] = allocated_lspace
            else:
                new_person["accomodated"] = needs_accomodation.upper()
                new_person["livingspace"] = "N/A"
            Amity.people_list.append(new_person)
            if allocated_office != "None":
                for room in Amity.room_list:
                    if room["name"] == allocated_office:
                        room["occupants"] += 1
            if allocated_lspace != "None" and needs_accomodation not in ["N", "NO"]:
                for room in Amity.room_list:
                    if room["name"] == allocated_lspace:
                        room["occupants"] += 1

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
        # get available office
        # get available lspace
        # check if the person exists
        # check if person is eligible for that room
        # get person's current office
        # get person's current living_space
        # check if prson is already in that room

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        if room_name.upper() not in [room["name"] for room in Amity.room_list]:
            print("%s does't exist." % room_name)
        else:
            occupants = [person["first_name"] + " " + person["last_name"] for
                         person in Amity.people_list if
                         person["office"] == room_name.upper() or
                         person["livingspace"] == room_name.upper()]
            if len(occupants) == 0:
                print("%s is empty" % room_name.upper())
            else:
                print(occupants)

    @staticmethod
    def print_allocations():
        """Prints all the people that have rooms and arranges by room"""
        no_office = [person["first_name"] + " " + person["last_name"]
                     for person in Amity.people_list
                     if person["office"] == "None"]
        no_livingspace = [person["first_name"] + " " + person["last_name"]
                          for person in Amity.people_list
                          if person["livingspace"] == "None"]
        print(no_office)
        print(no_office)

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
        pass
