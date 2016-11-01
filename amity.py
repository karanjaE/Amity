import random

from tabulate import tabulate

from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office


class Amity(object):
    """This class holds the system's core functionality"""
    rooms_list = {}
    people_list = {}

    @staticmethod
    def create_room(room_name, room_type):
        """Create a new room and adds it to the rooms list"""
        room_type = room_type.upper()
        room_name = room_name.upper()
        room_types = ["L", "l", "O", "o"]
        if room_type not in room_types:
            print("Dang!: Invalid room type entered. Use either O or L")
        elif len(room_name) == 0 or len(room_type) == 0:
            print("Make sure you enter all details. See help for more")
        elif not room_name.isalpha():
            print("Room name can only contain alphabets. Try again")
        elif room_name in Amity.rooms_list.keys():
            print("Dang! Name already taken. Enter another")
        elif room_type == "L":
            new_room = LivingSpace()
            Amity.rooms_list[room_name] = {}
            Amity.rooms_list[room_name]["Type"] = new_room.r_type
            Amity.rooms_list[room_name]["Capacity"] = new_room.capacity
            Amity.rooms_list[room_name]["Members"] = []
            print("Yay! %s created successfully." % room_name)
        elif room_type == "O":
            new_room = Office()
            Amity.rooms_list[room_name] = {}
            Amity.rooms_list[room_name]["Type"] = new_room.r_type
            Amity.rooms_list[room_name]["Capacity"] = new_room.capacity
            Amity.rooms_list[room_name]["Members"] = []
            print("Yay! %s created successfully." % room_name)
        return

    @staticmethod
    def generate_random_office():
        """Return a randomly selected office name from rooms_list"""
        rooms = Amity.rooms_list.keys()
        offices = []
        for room in rooms:
            if Amity.rooms_list[room]["Type"] == "OFFICE" and \
            len(Amity.rooms_list[room]["Members"]) < Amity.rooms_list[room]["Capacity"]:
                offices.append(room)
        if len(offices) == 0:
            return "None"
        elif len(offices) == 1:
            return offices[0]
        else:
            return random.choice(offices)

    @staticmethod
    def generate_random_living_space():
        """return a randomly selected living space"""
        rooms = Amity.rooms_list.keys()
        living_spaces = []
        for room in rooms:
            if Amity.rooms_list[room]["Type"] == "LIVINGSPACE" and \
            len(Amity.rooms_list[room]["Members"]) < Amity.rooms_list[room]["Capacity"]:
                living_spaces.append(room)
        if len(living_spaces) == 0:
            return "None"
        elif len(living_spaces) == 1:
            return living_spaces[0]
        else:
            return random.choice(living_spaces)

    @staticmethod
    def print_room(room_name):
        """Prints all the people ina given room"""
        room_name = room_name.upper()
        if room_name not in Amity.rooms_list:
            print("Sorry. %s does not exist" % room_name)
        room_members = Amity.rooms_list[room_name]["Members"]
        if len(room_members) == 0:
            print("Sorry. There's no one in %s" % room_name)
        else:
            table = Amity.rooms_list[room_name]["Members"]
            header = room_name
            print(tabulate(table, headers=header, tablefmt="simple"))
            return

    @staticmethod
    def add_person(first_name, last_name, designation, needs_accomodation="N"):
        """Add a new Person and randomly allocates appropriate rooms"""
        first_name = first_name.upper()
        last_name = last_name.upper()
        full_name = first_name + " " + last_name
        needs_accomodation = needs_accomodation.upper()
        needs = ["Y", "N"]
        designation = designation.upper()
        designations = ["S", "s", "F", "f"]
        office = Amity.generate_random_office()
        living_space = Amity.generate_random_living_space()
        if len(first_name) == 0 or len(last_name) == 0 \
        or len(designation) == 0:
            print("Please ensure all values are entered")
        elif not first_name.isalpha() or not last_name.isalpha():
            print("Names can only contain alphabets")
        elif designation not in designations:
            print("Please enter 'F' for fellow or 'S' for staff!")
        elif needs_accomodation not in needs:
            print("Needs Accomodation can only be Y or N")
        elif designation == "S" and needs_accomodation == "Y":
            print("Stop! Staff members can't opt in for accomodation!")
        elif designation == "S":
            new_person = Staff()
            Amity.people_list[full_name] = {}
            Amity.people_list[full_name]["Designation"] = new_person.designation
            Amity.people_list[full_name]["NeedsAccomodation"] = "NO"
            Amity.people_list[full_name]["Office"] = office
            Amity.people_list[full_name]["LivingSpace"] = "None"
            if office != "None":
                Amity.rooms_list[office]["Members"].append(full_name)
            print("%s successfully added." % full_name)
        elif designation == "F":
            new_person = Fellow()
            Amity.people_list[full_name] = {}
            Amity.people_list[full_name]["Designation"] = new_person.designation
            Amity.people_list[full_name]["Office"] = office
            if needs_accomodation == "N":
                Amity.people_list[full_name]["NeedsAccomodation"] = "NO"
                Amity.people_list[full_name]["LivingSpace"] = "None"
            elif needs_accomodation == "Y":
                Amity.people_list[full_name]["NeedsAccomodation"] = "YES"
                Amity.people_list[full_name]["LivingSpace"] = living_space

                if office != "None":
                    Amity.rooms_list[office]["Members"].append(full_name)
                if living_space != "None":
                    Amity.rooms_list[living_space]["Members"].append(full_name)
                print("%s successfully added." % full_name)

        return

    @staticmethod
    def remove_person(name):
        """Removes a person from Amity"""
        name = name.upper()
        if name not in Amity.people_list.keys():
            print("person does not exist!")
        else:
            opt = input("Deletes are irreversible. \n Are you sure?Y/N ").upper()
            if opt == "N":
                print("Phewks! I thought you were serious.")
            elif opt == "Y":
                current_office = Amity.people_list[name]["Office"]
                current_living_space = Amity.people_list[name]["LivingSpace"]
                del Amity.people_list[name]
                if not current_office == "None":
                    Amity.rooms_list[current_office]["Members"].remove(name)
                elif not current_living_space == "None":
                    Amity.rooms_list[current_living_space]["Members"].remove(name)
                print("%s successfully removed." % name)
            else:
                print("Invalid option")

        return

    @staticmethod
    def reallocate_person(name, room_type, new_room):
        """Moves a person to another room of their choice"""
        name = name.upper()
        room_type = room_type.upper()
        new_room = new_room.upper()
        room_types = ["L", "l", "O", "o"]
        if name not in Amity.people_list.keys():
            print("%s does not exist."%name)
        elif new_room not in Amity.rooms_list.keys():
            print("Room %s does not exist." % new_room)
        elif room_type not in room_types:
            print("Please select a valid room type(L or O)")
        elif len(Amity.rooms_list[new_room]["Members"]) >= \
        Amity.rooms_list[new_room]["Capacity"]:
            print("Sorry. %s  is already full" % new_room)
        elif Amity.people_list[name]["NeedsAccomodation"] == "NO" and room_type == "L":
            print("%s cannot get accomodation" % name)
        else:
            current_office = Amity.people_list[name]["Office"]
            current_living_space = Amity.people_list[name]["LivingSpace"]
            if room_type == "L":
                Amity.people_list[name]["LivingSpace"] = new_room
                Amity.rooms_list[new_room]["Members"].append(name)
                if current_living_space != "None":
                    Amity.rooms_list[current_living_space]["Members"].remove(name)
                print("%s successfully moved" % name)
            elif room_type == "O":
                Amity.people_list[name]["Office"] = new_room
                Amity.rooms_list[new_room]["Members"].append(name)
                if current_office != "None":
                    Amity.rooms_list[current_office]["Members"].remove(name)
                print("%s successfully moved" % name)

    @staticmethod
    def print_unallocated():
        """Prints all the people who have no rooms"""
        no_offices= []
        no_living_space = []
        for person in Amity.people_list.keys():
            if Amity.people_list[person]["Office"] == "None":
                no_offices.append(person)
            if Amity.people_list[person]["Designation"] == "FELLOW" and \
            Amity.people_list[person]["LivingSpace"] == "None":
                no_living_space.append(person)
        print("People with no offices \n", no_offices)
        print("People with no LivingSpace \n", no_living_space)
        return

    @staticmethod
    def print_allocations():
        """Prints all the rooms and their members"""
        print("All allocations \n++++++++++++++++")
        for room in Amity.rooms_list.keys():
            if len(Amity.rooms_list[room]["Members"]) > 0:
                print(room + Amity.rooms_list[room]["Members"])
        return

    @staticmethod
    def load_people(filename):
        """Loads people from a text file into the app"""
        pass

    @staticmethod
    def load_state(filename):
        """loads data from a specified filename and defaults to the default
        db if none is selected"""
        pass

    @staticmethod
    def save_state(filename):
        """persists app data to a specified db and defaults to def-db if None
        is selected"""
        pass
