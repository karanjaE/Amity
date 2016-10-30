import random

from db.migration import Person, Room
from rooms.rooms import Office, LivingSpace
from people.people import Fellow, Staff

rooms_list = {}
people_list = {}


def generate_random_l_space():
    """Generates a random room of living space type from the available rooms.
    """
    living_spaces = []
    r_lst = rooms_list.keys()

    if len(r_lst) < 1:
        return "None"
    elif len(r_lst) > 1:
        for room in r_lst:
            if rooms_list[room]["Capacity"] > len(rooms_list[room]["Members"]):
                if rooms_list[room]["Room Type"] == "LIVINGSPACE":
                    living_spaces.append(room)
    return random.choice(living_spaces)


def generate_random_office():
    """Generates a random office for allocation to people being added for the
    first time."""
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
    """The class holds the system's entire functionality"""

    @staticmethod
    def create_room(name, room_type):
        """Create a new room by declaring it's name and type"""
        rooms = rooms_list.keys()
        if name not in rooms:
            if room_type == "O":
                rooms_list[name] = {}
                office_space = Office()
                rooms_list[name]["Room Type"] = office_space.r_type
                rooms_list[name]["Capacity"] = office_space.capacity
                rooms_list[name]["Members"] = []
            elif room_type == "L":
                rooms_list[name] = {}
                living_space = LivingSpace()
                rooms_list[name]["Room Type"] = living_space.r_type
                rooms_list[name]["Capacity"] = living_space.capacity
                rooms_list[name]["Members"] = []
            else:
                return("Invalid room type. Enter O for office or L for livingspace.")
        else:
            print("Error: Room '%s' already exists" % name)

        return

    @staticmethod
    def add_person(fname, lname, designation, needs_acc="N"):
        """Add a new person and alocate them a random office, and if they are a
        fellow and have opted for accomodation, allocate them a random living
        space"""
        name = fname + " " + lname
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
        """Moves a person from one room to another
        """
        current_office = people_list[name]["Office"]
        current_l_space = people_list[name]["LivingSpace"]
        # Check if staff wants accomodation
        if people_list[name]["Designation"] == "STAFF" and room_type == "L":
            print("Error: Staff members can't get acommodation")
        #check if the selected room has accomodation
        elif len(rooms_list[new_room]["Members"]) >= \
        rooms_list[new_room]["Capacity"]:
            print("Error: The room you selected is already full")
        # check if the person is a staff and wants accomodation
        elif people_list[name]["Designation"] == "STAFF" and room_type == "L":
            print("A staff member cannot get accomodation")
        else:
            if room_type == "O":
                people_list[name]["Office"] = new_room
                rooms_list[new_room]["Members"].append(name)
            elif room_type == "L":
                if people_list[name]["NeedsAccomodation"] == "Y":
                    people_list[name]["LivingSpace"] = new_room
                    rooms_list[new_room]["Members"].append(name)
        #remove the person form the current list::
        if not current_office == "None":
            rooms_list[current_office]["Members"].remove(name)
        elif not current_l_space == "None":
            rooms_list[current_l_space]["Members"].remove(name)
        return

    @staticmethod
    def print_room(name):
        """Prints all the people in a given room.
        """
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
                unallocated["People with no Offices"].append(name)
            elif people_list[name]["LivingSpace"] == "None":
                unallocated["People with no Living Space"].append(name)
        return unallocated

    @staticmethod
    def load_people(filename):
        with open(filename, 'r') as people:
            for line in people:
                details = line.rstrip().split()
                name = details[0]+" "+details[1]
                designation = details[2]
                if len(details) <= 3:
                    needs_acc = "N"
                elif len(details) == 4:
                    needs_acc = details[3]
                people_list[name] = {}
                people_list[name]["Designation"] = designation
                people_list[name]["Needs Acc"] = needs_acc
                people_list[name]["Office"] = generate_random_office()
                if designation == "FELLOW" and needs_acc == "Y":
                    people_list[name]["LivingSpace"] = generate_random_l_space()
                else:
                    people_list[name]["LivingSpace"] = "None"
                if not people_list[name]["LivingSpace"] == "None" \
                and not people_list[name]["Office"] == "None":
                    rooms_list[people_list[name]["LivingSpace"]]["Members"].append(name)
                    rooms_list[people_list[name]["Office"]]["Members"].append(name)
            return

    @staticmethod
    def load_state(dbname='amity.db'):
        

    @staticmethod
    def save_state(dbname="main.db"):
        pass
