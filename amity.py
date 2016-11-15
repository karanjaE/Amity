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
    office_allocations = {"None":[]}
    lspace_allocations = {"None":[]}

    @staticmethod
    def create_room(room_type, room_name):
        """Creates an empty room of the specified type."""
        if not room_name.isalpha():
            print("Room name can only contain alphabets. Try again")
        if room_name.upper() in [room.name for room in Amity.room_list]:
            print("Dang! Name already taken. Enter another")
        else:
            mapping = {'O': Office, 'L': LivingSpace}
            new_room = mapping[room_type.upper()](room_name.upper())
            Amity.room_list.append(new_room)
            if room_type.upper() == "L":
                Amity.lspace_allocations[room_name.upper()] = []
            elif room_type.upper() == "O":
                Amity.office_allocations[room_name.upper()] = []
            print(room_name.upper() + " created successfully.")

    @staticmethod
    def generate_random_office():
        """Generates a random room of the given type."""
        offices = [room for room in Amity.room_list if room.type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.capacity > len(Amity.office_allocations[office.name]):
                available_offices.append(office.name)
        chosen_room = "None"
        if len(available_offices):
            chosen_room = random.choice(available_offices)
        return chosen_room

    @staticmethod
    def generate_random_lspace():
        lspaces = [room for room in Amity.room_list if room.type == "LIVINGSPACE"]
        available_l_spaces = []
        for lspace in lspaces:
            if lspace.capacity > len(Amity.lspace_allocations[lspace.name]):
                available_l_spaces.append(lspace.name)
        chosen_room = "None"
        if len(available_l_spaces):
            chosen_room = random.choice(available_l_spaces)
        return chosen_room

    @staticmethod
    def add_person(first_name, last_name, designation, needs_accomodation="N"):
        """Adds a new person and allocates a random room to them."""
        if not first_name.isalpha() or not last_name.isalpha():
            print("Error! Names can only have alphabets!")
        elif designation.upper() not in ['S', 'STAFF', 'F', 'FELLOW']:
            print("Invalid designation. Enter F or FELLOW or S or STAFF")
        elif needs_accomodation.upper() not in ['Y', 'N']:
            print("Invalid option. Enter a valid accomodation request option!")
        elif (designation.upper() in ["S", "STAFF"] and
              needs_accomodation.upper() == "Y"):
            print("Staff members cannot get accomodation!")
        else:
            allocated_office = Amity.generate_random_office()
            mapping = {"F": Fellow, "S": Staff, "FELLOW": Fellow, "STAFF": Staff}
            person_id = len(Amity.people_list) + 1
            new_person = mapping[designation.upper()](person_id, first_name.upper(),
                                                      last_name.upper(),
                                                      designation.upper())
            Amity.people_list.append(new_person)
            Amity.office_allocations[allocated_office].append(first_name
                                                              + " " + last_name)
            if needs_accomodation.upper() == "Y" and designation.upper() == "F":
                allocated_lspace = Amity.generate_random_lspace()
                Amity.lspace_allocations[allocated_lspace].append(first_name
                                                                  + " " + last_name)
            print(first_name.upper() + " " + last_name.upper() +
                  " added successfully")

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
    def reallocate_person(fname, lname, room_type, new_room):
        """Moves a person to another room"""
        # available_offices = [room for room in Amity.office_allocations.keys()
        #                      if len(Amity.office_allocations[room]) < 6
        #                      and room != "None"]
        # available_lspaces = [room for room in Amity.lspace_allocations.keys()
        #                      if len(Amity.lspace_allocations[room]) < 4
        #                      and room != "None"]
        # name = fname + " " + lname
        # if room_type.upper() == "L":
        pass

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        if room_name.upper() in Amity.office_allocations.keys():
            print("=" * 30 + "\n" + room_name.upper() + "\n" + "=" * 30)
            if not len(Amity.office_allocations[room_name.upper()]):
                print("Empty")
            else:
                for person in Amity.office_allocations[room_name.upper()]:
                    print(person)
        elif room_name.upper() in Amity.office_allocations.keys():
            print("=" * 30 + "\n" + room_name.upper() + "\n" + "=" * 30)
            if not len(Amity.lspace_allocations[room_name.upper()]):
                print("Empty")
            else:
                for person in Amity.lspace_allocations[room_name.upper()]:
                    print(person)
        else:
            print("The room does not exist")

    @staticmethod
    def print_unallocated(filename=None):
        """Prints all the people that have no rooms and arranges by room"""
        unallocated_office = Amity.office_allocations["None"]
        unallocated_lspace = Amity.lspace_allocations["None"]
        print("=" * 30 + "\n" + "No Office\n" + "=" * 30)
        for person in unallocated_office:
            print(person or "None")
        print("=" * 30 + "\n" + "No LivingSpace\n" + "=" * 30)
        for person in unallocated_lspace:
            print(person or "None")

        if filename:
            file = open(filename + ".txt", "a")
            file.write("=" * 30 + "\n" + "No Office\n" + "=" * 30)
            for person in unallocated_office:
                file.write("\n" + person or "None")
            file.write("\n" + "=" * 30 + "\n" + "No LivingSpace\n" + "=" * 30)
            for person in unallocated_lspace:
                file.write("\n" + person or "None")
            print("%s.txt written successfully" % filename)

    @staticmethod
    def print_allocations(filename=None):
        """Prints all the people who have rooms"""
        print("=" * 30 + "\n" + "Office Allocations\n" + "=" * 30)
        for room in Amity.office_allocations.keys():
            if room != "None":
                print(room + "\n" + "+" * 30)
                for person in Amity.office_allocations[room]:
                    print(person)
        print("=" * 30 + "\n" + "LivingSpace Allocations\n" + "=" * 30)
        for room in Amity.lspace_allocations.keys():
            if room != "None":
                print(room + "\n" + "+" * 30)
                for person in Amity.lspace_allocations[room]:
                    print(person)

        if filename:
            file = open(filename + ".txt", "a")
            file.write("=" * 30 + "\n" + "Office Allocations\n" + "=" * 30)
            for room in Amity.office_allocations.keys():
                if room != "None":
                    file.write(room + "\n" + "+" * 30)
                    for person in Amity.office_allocations[room]:
                        file.write(person)
            file.write("=" * 30 + "\n" + "LivingSpace Allocations\n" + "=" * 30)
            for room in Amity.lspace_allocations.keys():
                if room != "None":
                    file.write(room + "\n" + "+" * 30)
                    for person in Amity.lspace_allocations[room]:
                        file.write(person)
            print("%s.txt written" % filename)

    @staticmethod
    def load_state(dbname=None):
        """Loads data from a DB file into the app."""
        engine = create_engine("sqlite:///" + dbname + ".sqlite")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        people = session.query(Person).all()
        rooms = session.query(Room).all()
        if not dbname:
            print("You must select a db to load.")
        else:
            for room in rooms:
                loaded_room = {}
                loaded_room["name"] = room.name
                loaded_room["type"] = room.r_type
                loaded_room["capacity"] = room.capacity
                loaded_room["occupants"] = room.occupants
                Amity.room_list.append(loaded_room)
            for person in people:
                loaded_person = {}
                loaded_person["id"] = person.person_id
                loaded_person["first_name"] = person.first_name
                loaded_person["last_name"] = person.last_name
                loaded_person["accomodated"] = person.accomodated
                loaded_person["designation"] = person.designation
                loaded_person["office"] = person.office
                loaded_person["livingspace"] = person.l_space
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
