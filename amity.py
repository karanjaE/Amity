import os
import random
import sys

from tabulate import tabulate

from db import migration
from rooms.rooms import Office, LivingSpace
from people.people import Fellow, Staff

rooms_list = {}
people_list = {}

def generate_random_l_space():
    l_spaces = []
    r_lst = rooms_list.keys()
    if len(r_lst) < 1:
        return "None"
    elif len(r_lst) > 1:
        for room in r_lst:
            if rooms_list[room]["Capacity"] > len(rooms_list[room]["Members"]):
                if rooms_list[room]["Room Type"] == "LIVINGSPACE":
                    l_spaces.append(room)
        return random.choice(l_spaces)


def generate_random_office():
    o_spaces = []
    r_lst = rooms_list.keys()
    if len(r_lst) < 1:
        return "None"
    elif len(r_lst) > 1:
        for room in r_lst:
            if rooms_list[room]["Capacity"] > len(rooms_list[room]["Members"]):
                if rooms_list[room]["Room Type"] == "OFFICE":
                    o_spaces.append(room)
        return random.choice(o_spaces)


class Amity(object):

    @staticmethod
    def create_room(name, room_type):
        rooms_list[name] = {}
        if room_type == "O":
            office_space = Office()
            rooms_list[name]["Room Type"] = office_space.r_type
            rooms_list[name]["Capacity"] = office_space.capacity
            rooms_list[name]["Members"] = []
        elif room_type == "L":
            living_space = LivingSpace()
            rooms_list[name]["Room Type"] = living_space.r_type
            rooms_list[name]["Capacity"] = living_space.capacity
            rooms_list[name]["Members"] = []
        else:
            return("Invalid room type. Enter O for office or L for livingspace.")

        return

    @staticmethod
    def add_person(name, designation, needs_acc="N"):
        people_list[name] = {}
        random_office = generate_random_office()
        random_l_space = generate_random_l_space()
        if designation == "S":
            staff = Staff()
            people_list[name]["Designation"] = staff.designation
            people_list[name]["NeedsAccomodation"] = needs_acc
            people_list[name]["Office"] = random_office
            people_list[name]["LivingSpace"] = "None"
            if not random_office == "None":
                rooms_list[random_office]["Members"].append(name)
        elif designation == "F":
            fellow = Fellow()
            people_list[name]["Designation"] = fellow.designation
            people_list[name]["NeedsAccomodation"] = needs_acc
            people_list[name]["Office"] = random_office
            if needs_acc == "N":
                people_list[name]["LivingSpace"] = "None"
            elif needs_acc == "Y":
                people_list[name]["LivingSpace"] = random_l_space
            # Add person name to room members
            if not random_l_space == "None" and not random_office == "None":
                rooms_list[random_l_space]["Members"].append(name)
                rooms_list[random_office]["Members"].append(name)

        else:
            print("Error: Invalid designation")

        return

    @staticmethod
    def reallocate_person(name, room_type, new_room):
        if room_type == "O":
            current_office = people_list[name]["Office"]
            if len(rooms_list[new_room]["Members"]) < rooms_list[new_room]["Capacity"]:
                rooms_list[current_office]["Members"].remove(name)
                people_list[name]["Office"] = new_room
                rooms_list[new_room]["Members"].append(name)
                print("%s reallocated to %s" % (name, new_room))
        elif room_type == "L":
            if people_list[name]["Designation"] == "STAFF":
                print("Error: Staff members cannot have accomodation!")
            elif(people_list[name]["Designation"] == "FELLOW") and (people_list[name]["NeedsAccomodation"] == "N"):
                print("%s opted for NO ACCOMODATION. Can't reallocate" % name)
            else:
                current_l_space = people_list[name]["LivingSpace"]
                if len(rooms_list[new_room]["Members"]) < rooms_list[new_room]["Capacity"]:
                    rooms_list[current_l_space]["Members"].remove(name)
                    people_list[name]["LivingSpace"] = new_room
                    rooms_list[new_room]["Members"].append(name)
                    print("%s reallocated to %s" % (name, new_room))


    def remove_person(name):
        #remove from office
        cur_office = people_list[name]["Office"]
        rooms_list[cur_office]["Members"].remove(name)
        #remove from l_space
        if people_list[name]["Designation"] == "FELLOW":
            cur_l_room = people_list[name]["LivingSpace"].remove(name)

        #delete record
        del people_list[name]
        return

    @staticmethod
    def print_room(name):
        all_rooms = rooms_list.keys()
        if name not in all_rooms:
            print("Error: Room doesn't exist")
        else:
            print("Showing members in %s:" % name)
            print(rooms_list[name]["Members"])
        return

    @staticmethod
    def print_allocations():
        r_lst = rooms_list.keys()
        allocations = {}
        for room in r_lst:
            if len(rooms_list[room]["Members"]) > 0:
                allocations[room]={}
                allocations[room]["Members"] = rooms_list[room]["Members"]
        return allocations

    @staticmethod
    def print_unallocated(output_file=None):
        unallocated = {}
        unallocated["Office Unallocated People"] = []
        unallocated["People with no Living Space"] = []
        people_lst = people_list.keys()
        for name in people_lst:
            if people_list[name]["Office"] == "None":
                unallocated["Office Unallocated People"].append(name)
            elif people_list[name]["LivingSpace"] == "None":
                unallocated["People with no Living Space"].append(name)
        return unallocated

    @staticmethod
    def load_people(filename):
        rand_office = generate_random_office()
        rand_l_space = generate_random_l_space()
        with open(filename) as pfile:
            for line in pfile:
                details = line.rstrip().split()
                name = details[0]+" "+details[1]
                designation = details[2]
                people_list[name] = {}
                if len(details) < 4:
                    needs_acc = "N"
                else:
                    needs_acc = designation[3]

                if designation == "STAFF":
                    staff = Staff()
                    people_list[name]["Designation"] = staff.designation
                    people_list[name]["NeedsAccomodation"] = staff.needs_acc
                    people_list[name]["Office"] = rand_office
                    people_list[name]["LivingSpace"] = "None"

                    if not people_list[name]["Office"] == "None":
                        rooms_list[rand_office]["Members"].append(name)
                elif designation == "FELLOW":
                    fellow = Fellow()
                    people_list[name]["Designation"] = fellow.designation
                    people_list[name]["NeedsAccomodation"] = needs_acc
                    people_list[name]["Office"] = rand_office
                    if needs_acc == "N":
                        people_list[name]["LivingSpace"] = "None"
                    elif needs_acc == "Y":
                        people_list[name]["LivingSpace"] = rand_l_space

                    if not people_list[name]["Office"] == "None" and not people_list[name]["LivingSpace"] == "None":
                        rooms_list[rand_office]["Members"].append(name)
                        rooms_list[rand_office]["Members"].append(name)
            return

    @staticmethod
    def load_state(dbname='amity.db'):
        pass


    def save_state(dbname=None):
        #save people to the db.
        for key in people_list:
            name = key
            needs_acc = people_list[key]["NeedsAccomodation"]
            designation = people_list[key]["Designation"]
            office = people_list[key]["Office"]
            l_space = people_list[key]["LivingSpace"]

        #Save rooms data to the db
        for key in rooms_list:
            name =  key
            capacity = rooms_list[key]["Capacity"]
            room_type = rooms_list[key]["Room Type"]
            members = rooms_list[key]["Members"]
