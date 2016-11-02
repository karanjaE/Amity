import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from db.migration import Base, Person, Room, DatabaseCreator
from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office


class Amity:
    people_list = []
    room_list = []

    @staticmethod
    def create_room(room_name, room_type):
        """Creates an empty room of the specified type."""
        room_types = ["L", "O"]
        if room_type.upper() not in room_types:
            print("Dang!: Invalid room type entered. Use either O or L")
        elif not room_type or not room_name:
            print("Make sure you enter all details. See help for more")
        elif not room_name.isalpha():
            print("Room name can only contain alphabets. Try again")
        elif room_name in Amity.room_list:
            print("Dang! Name already taken. Enter another")
        else:
            new_room = {}
            new_room["Name"] = room_name

    @staticmethod
    def generate_random_room(room_type):
        """Generates a random room of the given type."""
        pass

    @staticmethod
    def add_person(first_name, last_name, designation, needs_accomodation):
        """Adds a new person and allocates a random room to them."""
        pass

    @staticmethod
    def load_people(filename):
        """Loads people from a file.txt into the app and creates them"""
        pass

    @staticmethod
    def reallocate_person(full_name, room_type, new_room):
        """Moves a person to another room"""
        pass

    @staticmethod
    def remove_person(full_name):
        """Removes a person from the system"""
        pass

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        pass

    @staticmethod
    def print_allocations():
        """Prints all rooms and people allocated to them."""
        pass

    @staticmethod
    def print_unallocated():
        """Prints all the people who don't have rooms"""
        pass

    @staticmethod
    def load_state():
        """Loads data from a DB file into the app."""
        pass

    @staticmethod
    def save_state():
        """Persists data saved in the app to a db"""
        pass
