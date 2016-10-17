import random

from rooms.rooms import Office, LivingSpace
from people.people import Fellow, Staff

rooms_list = {}
people_list = {}
class Amity(object):
    

    @staticmethod
    def  create_room(name, r_type):
        rooms_list[name] = {}
        if r_type == "O":
            office_space = Office()
            rooms_list[name]["Room Type"] = office_space.r_type
            rooms_list[name]["Capacity"] = office_space.capacity
            rooms_list[name]["Menbers"] = []
        elif r_type == "L":
            living_space = LivingSpace()
            rooms_list[name]["Room Type"] = living_space.r_type
            rooms_list[name]["Capacity"] = living_space.capacity
            rooms_list[name]["Members"] = []
        else:
            return("Invalid room type. Enter O for office or L for livingspace.")

        return

    @staticmethod
    def generate_random_room():
        av_rooms = []
                


    def add_person(name, designation):
        pass


    def reallocate_person(name, r_type, new_room):
        pass


    def remove_person(name):
        pass


    def print_room(name):
        pass


    def print_allocations():
        pass


    def print_unallocated():
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

print(rooms_list)
