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
    def create_room(room_type, room_name):
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
            new_person["id"] = str(len(Amity.people_list) + 1)
            new_person["first_name"] = first_name.upper()
            new_person["last_name"] = last_name.upper()
            if designation.upper() in ["F", "FELLOW"]:
                new_person["designation"] = "FELLOW"
            elif designation.upper() in ["S", "STAFF"]:
                new_person["designation"] = "STAFF"
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
            print("File loaded.")

    @staticmethod
    def reallocate_person(person_id, room_type, new_room):
        """Moves a person to another room"""
        if str(person_id) not in [p["id"] for p in Amity.people_list]:
            print("Person doesn't exist!")
        else: print("The person exists")

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        if room_name.upper() not in [room["name"] for room in Amity.room_list]:
            print("%s does't exist." % room_name)
        else:
            occupants = [person["id"] + " " + person["first_name"] + " " +
                         person["last_name"] for
                         person in Amity.people_list if
                         person["office"] == room_name.upper() or
                         person["livingspace"] == room_name.upper()]
            if len(occupants) == 0:
                print("%s is empty" % room_name.upper())
            else:
                print("People in %s\n===================" % room_name.upper())
                for occupant in occupants:
                    print(occupant)

    @staticmethod
    def print_unallocated(filename=None):
        """Prints all the people that have rooms and arranges by room"""
        no_office = [person["id"] + " " +
                     person["first_name"] + " " + person["last_name"]
                     for person in Amity.people_list
                     if person["office"] == "None"]
        no_livingspace = [person["id"] + " " +
                          person["first_name"] + " " + person["last_name"]
                          for person in Amity.people_list
                          if person["livingspace"] == "None"]
        print("\n==============\nNo LivingSpace:\n==============")
        for person in no_livingspace:
            print(person)
        print("\n==============\nNo Office\n==============")
        for person in no_office:
            print(person)
        if filename:
            file = open(filename + ".txt", "a")
            file.write("\n==============\nNo LivingSpace:\n==============\n")
            for person in no_livingspace:
                file.write(person)
                file.write("\n")
            file.write("\n==============\nNo Office\n==============\n")
            for person in no_office:
                file.write(person)
                file.write("\n")
            print("%s.txt written successfully" % filename)

    @staticmethod
    def print_allocations(filename=None):
        """Prints all the people who don't have rooms"""
        all_rooms = [room["name"] for room in Amity.room_list]
        for room in all_rooms:
            members = [person["id"] + " " +
                       person["first_name"] + " " + person["last_name"] for
                       person in Amity.people_list if
                       person["office"] == room or person["livingspace"] == room]
            if len(members) == 0:
                print("\n\n================\n" + room + "\n================")
                print("Empty")
            else:
                print("\n\n================\n" + room + "\n================")
                for member in members:
                    print(member)
                if filename:
                    file = open(filename + ".txt", "a")
                    file.write("\n\n===============\n%s\n===============\n" %room)
                    for member in members:
                        file.write(member)
                        file.write("\n")

    @staticmethod
    def load_state(dbname=None):
        """Loads data from a DB file into the app."""
        engine=create_engine("sqlite:///" + dbname + ".sqlite")
        Session=sessionmaker()
        Session.configure(bind=engine)
        session=Session()
        people=session.query(Person).all()
        rooms=session.query(Room).all()
        if not dbname:
            print("You must select a db to load.")
        else:
            for room in rooms:
                loaded_room={}
                loaded_room["name"]=room.name
                loaded_room["type"]=room.r_type
                loaded_room["capacity"]=room.capacity
                loaded_room["occupants"]=room.occupants
                Amity.room_list.append(loaded_room)
            for person in people:
                loaded_person={}
                loaded_person["id"]=person.person_id
                loaded_person["first_name"]=person.first_name
                loaded_person["last_name"]=person.last_name
                loaded_person["accomodated"]=person.accomodated
                loaded_person["designation"]=person.designation
                loaded_person["office"]=person.office
                loaded_person["livingspace"]=person.l_space
                Amity.people_list.append(loaded_person)
            print("Data from %s loaded to the app." % dbname)

    @staticmethod
    def save_state(db_name=None):
        """Persists data saved in the app to a db"""
        if not db_name:
            db = DatabaseCreator()
        else:
            db = DatabaseCreator(db_name)
        Base.metadata.bind = db.engine
        db_session = db.session()
        for room in Amity.room_list:
            room_to_save = Room(
                name=room["name"],
                r_type=room["type"],
                capacity=room["capacity"],
                occupants=room["occupants"]
            )
            db_session.merge(room_to_save)
        for person in Amity.people_list:
            person_to_save = Person(
                person_id=person["id"],
                first_name=person["first_name"],
                last_name=person["last_name"],
                accomodated=person["accomodated"],
                designation=person["designation"],
                office=person["office"],
                l_space=person["livingspace"]
            )
            db_session.merge(person_to_save)
        db_session.commit()
