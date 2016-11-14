from amity import *

from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office


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
                people_list[name]["NeedsAccomodation"] = fellow.needs_acc
                people_list[name]["Office"] = rand_office
                if needs_acc == "N":
                    people_list[name]["LivingSpace"] = "None"
                elif needs_acc == "Y":
                	people_list[name]["LivingSpace"] = rand_l_space

                if not people_list[name]["Office"] == "None" and not people_list[name]["LivingSpace"] == "None":
                	rooms_list[rand_office]["Members"].append(name)
                	rooms_list[rand_office]["Members"].append(name)
        return


def save_state(dbname=None):
	for key in people_list:
		name = key
		needs_acc = people_list[key]["NeedsAccomodation"]
		designation = people_list[key]["Designation"]
		office = people_list[key]["Office"]
		l_space = people_list[key]["LivingSpace"]


	for key in rooms_list:
		name = key
		capacity = rooms_list[key]["Capacity"]
		room_type = rooms_list[key]["Room Type"]
		members = rooms_list[key]["Members"]
