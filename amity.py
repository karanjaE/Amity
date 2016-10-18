import random

from tabulate import tabulate

from rooms.rooms import Office, LivingSpace
from people.people import Fellow, Staff

rooms_list = {}
people_list = {}

def generate_random_l_space():
    l_spaces = []
    r_lst = rooms_list.keys()
    for room in r_lst:
        if rooms_list[room]["Capacity"] > len(rooms_list[room]["Members"]):
            if rooms_list[room]["Room Type"] == "LIVINGSPACE":
                l_spaces.append(room)
    return random.choice(l_spaces)


def generate_random_office():
    o_spaces = []
    r_lst = rooms_list.keys()
    for room in r_lst:
        if rooms_list[room]["Capacity"] > len(rooms_list[room]["Members"]):
            if rooms_list[room]["Room Type"] == "OFFICE":
                o_spaces.append(room)
    return random.choice(o_spaces)


class Amity(object):

    @staticmethod
    def create_room(name, r_type):
        rooms_list[name] = {}
        if r_type == "O":
            office_space = Office()
            rooms_list[name]["Room Type"] = office_space.r_type
            rooms_list[name]["Capacity"] = office_space.capacity
            rooms_list[name]["Members"] = []
        elif r_type == "L":
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
            rooms_list[random_l_space]["Members"].append(name)
            rooms_list[random_office]["Members"].append(name)

        else:
            print("Error: Invalid designation")

        return

    @staticmethod
    def reallocate_person(name, r_type, new_room):
        if r_type == "O":
            current_office = people_list[name]["Office"]
            if len(rooms_list[new_room]["Members"]) < rooms_list[new_room]["Capacity"]:
                rooms_list[current_office]["Members"].remove(name)
                people_list[name]["Office"] = new_room
                rooms_list[new_room]["Members"].append(name)
                print("%s reallocated to %s" % (name, new_room))
        elif r_type == "L":
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
                    print("%s reallocated to %s" % name, new_room)


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
    def print_unallocated():
        # unallocated = {}
        # p_lst = people_list.keys()
        # for person in p_lst:
        #     if people_list[person]["OFFICE"] == "None":
        #         unallocated[person]["OFFICE"] = "None"
        pass

    def load_people(filename):
        pass

    def load_state(dbname):
        pass

    def save_state(dbname):
        pass


Amity.create_room("Valhalla", "O")
Amity.create_room("Higwarts", "L")
Amity.create_room("Jail", "L")
Amity.create_room("Narnia", "O")
Amity.create_room("Vale", "L")
Amity.create_room("Mordor", "O")
Amity.create_room("Avatar", "L")

Amity.add_person("Drew", "F", "Y")
Amity.add_person("Jay", "S")
Amity.add_person("Bob", "F", "Y")
Amity.add_person("Hatty", "S")
Amity.add_person("Shee", "F")

# print("+++++++++++++++++\n+++++++++++++")
print(rooms_list)
print("+++++++++++++++++\n+++++++++++++")
print(people_list)


Amity.reallocate_person("Drew", "O", "Valhalla")


# print("+++++++++++++++++\n+++++++++++++")
print(rooms_list)
print("+++++++++++++++++\n+++++++++++++")
print(people_list)

# # Amity.print_room("Vale")

# # print("+++++++++++++++++\n+++++++++++++")
# # print("+++++++++++++++++\n+++++++++++++")
# # print(Amity.print_allocations())

