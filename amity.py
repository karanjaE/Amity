import os
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from db.migration import (Base, Person, Room, DatabaseCreator,
                          OfficeAllocations, LivingSpaceAllocations)
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
        offices = [room for room in Amity.room_list if room.r_type == "OFFICE"]
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
        lspaces = [room for room in Amity.room_list if room.r_type == "LIVINGSPACE"]
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
        allocated_office = Amity.generate_random_office()
        mapping = {"F": Fellow, "S": Staff}
        person_id = len(Amity.people_list) + 1
        new_person = mapping[designation.upper()](person_id, first_name.upper(),
                                                  last_name.upper(),
                                                  designation)
        Amity.people_list.append(new_person)
        Amity.office_allocations[allocated_office].append(first_name.upper()
                                                          + " " + last_name.upper())
        if needs_accomodation.upper() == "Y" and designation.upper() == "F":
            allocated_lspace = Amity.generate_random_lspace()
            Amity.lspace_allocations[allocated_lspace].append(first_name.upper()
                                                              + " " + last_name.upper())
        print("Success!")

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
    def reallocate_person(fname, lname, room_type, new_room):
        """Moves a person to another room"""
        full_name = fname.upper() + " " + lname.upper()
        fellows = [p.name for p in Amity.people_list
                   if p.designation == "FELLOW"]
        staff = [p.name for p in Amity.people_list
                 if p.designation == "STAFF"]
        av_lspaces = [r.name for r in Amity.room_list
                      if r.r_type == "LIVINGSPACE"
                      and len(Amity.lspace_allocations[r.name]) < 4]
        av_offices = [r.name for r in Amity.room_list
                      if r.r_type == "OFFICE"
                      and len(Amity.office_allocations[r.name]) < 6]
        if full_name not in fellows and full_name not in staff:
            print("The person doesn't exist.")
        elif new_room.upper() not in av_lspaces and new_room.upper() not in av_offices:
            print("The room requested does not exist or is not available")
            print("Available Offices \n" + av_offices)
            print("Available living spaces\n" + av_lspaces)
        else:
            if room_type.upper() == "L":
                if new_room in av_offices and new_room not in av_lspaces:
                    print("The room selected is not a LivingSpace.")
                elif full_name not in fellows:
                    return("The person has to exist and be a fellow!")
                else:
                    for room in Amity.lspace_allocations.keys():
                        if full_name in Amity.lspace_allocations[room]:
                            cur_lspace = Amity.lspace_allocations[room]
                            cur_lspace.remove(full_name)
                            Amity.lspace_allocations[new_room.upper()].append(full_name)
                            print("Success!")
            elif room_type.upper() == "O":
                if new_room not in av_offices and new_room in av_lspaces:
                    print("The room selected is not an office")
                else:
                    for room in Amity.lspace_allocations.keys():
                        if full_name in Amity.office_allocations[room]:
                            cur_office = Amity.office_allocations[room]
                            cur_office.remove(full_name)
                            Amity.office_allocations[new_room.upper()].append(full_name)
                            print("Success!")

    @staticmethod
    def print_room(room_name):
        """Returns all the members of a given room"""
        offices = [room for room in Amity.office_allocations
                   if room != "None"]
        lspaces = [room for room in Amity.lspace_allocations
                   if room != "None"]
        if room_name.upper() not in offices and room_name.upper() not in lspaces:
            print("The room doesn't exist")
        else:
            print("=" * 30 + "\nMembes\n" + "=" * 30)
            if room_name.upper() in offices:
                for person in Amity.office_allocations[room_name.upper()]:
                    print(person)
            elif room_name.upper() in lspaces:
                for person in Amity.lspace_allocations[room_name.upper()]:
                    print(person)

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
        office_allocations = session.query(OfficeAllocations)
        lspace_allocations = session.query(LivingSpaceAllocations)
        if not dbname:
            print("You must select a db to load.")
        else:
            for room in rooms:
                Amity.room_list.append(room)
            for person in people:
                Amity.people_list.append(person)
            for office_allocation in office_allocations:
                all_members = office_allocation.members.split(",")
                Amity.office_allocations[office_allocation.room_name] = all_members
            for lspace_allocation in lspace_allocations:
                all_members = lspace_allocation.members.split(",")
                Amity.lspace_allocations[lspace_allocation.room_name] = all_members

            print("Data from %s loaded to the app." % dbname)

    @staticmethod
    def save_state(db_name=None):
        """Persists data saved in the app to a db"""
        if not db_name:
            db = DatabaseCreator("default_db")
        else:
            db = DatabaseCreator(db_name)
        Base.metadata.bind = db.engine
        db_session = db.session()
        for room in Amity.room_list:
            room_to_save = Room(
                name=room.name,
                rtype=room.r_type,
                capacity=room.capacity
            )
            db_session.merge(room_to_save)
        for person in Amity.people_list:
            person_to_save = Person(
                # person_id=person.person_id,
                name=person.name,
                designation=person.designation
            )
            db_session.merge(person_to_save)
        for room in Amity.office_allocations:
            office_members = ",".join(Amity.office_allocations[room])
            office_allocations_sv = OfficeAllocations(
                room_name=room,
                members=office_members
            )
            db_session.merge(office_allocations_sv)
        for room in Amity.lspace_allocations:
            lspace_members = ",".join(Amity.lspace_allocations[room])
            lspace_allocations_sv = LivingSpaceAllocations(
                room_name=room,
                members=lspace_members
            )
            db_session.merge(lspace_allocations_sv)
        db_session.commit()
        print("Success!")
