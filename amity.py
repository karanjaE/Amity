import random
import tabulate

from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office

rooms_list = dict()
person_list = dict()

class Amity(object):
	"""Holds all the core functionalities of the app
	"""
	def __init__(self):
		pass

	def create_room(self,room_name, r_type):
		"""Creates a new room. Depending on which argument is passes, the 
		room can either be a (L)LivingSpace or (O)Office
		"""
		rooms_list[room_name] = dict()
		# rtype = input("enter type: ")
		if r_type == 'L':
			livingspace = LivingSpace()
			rooms_list[room_name]["Type"] = livingspace.r_type
			rooms_list[room_name]["Capacity"] = livingspace.capacity
			rooms_list[room_name]["Occupants"] = []
		elif r_type == "O":
			officespace = Office()
			rooms_list[room_name]["Name"] = room_name
			rooms_list[room_name]["Type"] = officespace.r_type
			rooms_list[room_name]["Capacity"] = officespace.capacity
			rooms_list[room_name]["Occupants"] = []
		else:
			return("Invalid room type")

		return


	def gen_available_offices(self):
		"""Generates a list of available offices
		"""
		self.av_rooms = []
		rlst = rooms_list.keys()
		indx = 0
		pips = len(rooms_list[rlst[indx]]["Occupants"])
		print pips
		cap = rooms_list[rlst[indx]]["Capacity"]
		print cap
		nm = rooms_list[rlst[indx]]["Name"]
		print nm
		while indx < len(rlst):
			if pips < cap:
				self.av_rooms.append(nm)
				indx += 1
		l = (set(self.av_rooms))
		return list(l)
		


	def allocate_random_office(self):
		"""Returns a randomly selected office
		"""
		all_rooms = self.gen_available_offices()
		# print ("AV", av_rooms)
		k = random.randint(0, len(all_rooms)-1)
		return all_rooms[k]

	def add_person(self, person_name, person_desig):
		"""Creates a new person, allocates a random office and if they are
		Fellow, allows them to request for accomodation by passing (Y) as 
		an argument for needs_accomodation
		"""
		person_list[person_name] = dict()
		randroom = self.allocate_random_office()
		# check if person is staff or fellow and act
		if person_desig == "S":
			staff = Staff()
			person_list[person_name]["Designation"] = staff.person_desig
			person_list[person_name]["Needs Accomodation"] = "No"
			person_list[person_name]["LivingSpace"] = "None"
			person_list[person_name]["Office"] = randroom
		elif person_des == "F":
			fellow = Fellow()
			ans = input("Does %s need accomodation?(Y/N): " % person_name)
			person_list[person_name]["Designation"] = fellow.person_desig
			person_list[person_name]["Needs Accomodation"] = ans
			person_list[person_name]["LivingSpace"] = "None"
			person_list[person_name]["Office"] = randroom
		else:
			return("Invalid designation")

		
		#Add person to room occupants
		rooms_list[randroom]["Occupants"].append(person_name)
		return

		    




	def reallocate_person(self, person, r_type, new_room):
		"""Reassigns a different room to a person.
		option L changes living space and option O changes office
		"""
		pass



	def print_allocations(self):
		"""Print each room and the people in it
		pass
		"""

	def print_unallocated(self):
		"""Print all Fellows with no accomodation
		"""
		pass

	def print_room(self):
		"""Print all the people in a specified room
		"""
		pass

	def delete_person(self):
		"""remove a person and release the space in the room/s that 
		had been allocated to them
		"""
		pass

	def load_people(self):
		"""gets people from a file.txt and adds them
		"""
		pass

	def load_state(self):
		"""Loads data from an sqlite db into the app
		"""
		pass

	def save_state(self):
		"""Persist data stored in the app into a SQLite DB
		"""
		pass




		

ed = Amity()
ed.create_room("Hi", "L")
ed.create_room("Kked", "O")
ed.create_room("Jain", "O")
ed.create_room("Kry", "L")



k = Amity()
k.add_person("Eddy", "S")
k = Amity()
k.add_person("JJ", "S")

print(person_list)


print(rooms_list)
print("Output", k.gen_available_offices())