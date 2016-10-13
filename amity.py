import random
import tabulate

from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office

class Amity(object):
	"""Holds all the core functionalities of the app
	"""
	def __init__(self):
		self.rooms_list = []
		self.person_list = []

	def create_room(self,room_name, r_type):
		"""Creates a new room. Depending on which argument is passes, the 
		room can either be a (L)LivingSpace or (O)Office
		"""
		room_dict = dict()
		# rtype = input("enter type: ")
		if r_type == 'L':
			livingspace = LivingSpace()
			room_dict["Name"] = room_name
			room_dict["Type"] = livingspace.r_type
			room_dict["Capacity"] = livingspace.capacity
		elif r_type == "O":
			officespace = Office()
			room_dict["Name"] = room_name
			room_dict["Type"] = officespace.r_type
			room_dict["Capacity"] = officespace.capacity
		else:
			return("Invalid room type")

		self.rooms_list.append(room_dict)
		print(self.rooms_list)

	def add_person(self, person_name, person_desig):
		"""Creates a new person, allocates a random office and if they are
		Fellow, allows them to request for accomodation by passing (Y) as 
		an argument for needs_accomodation
		"""
		person_dict = dict()
		# check if person is staff or fellow and act
		if person_des == "S":
			staff = Staff()
			person_dict["Name"] = person_name
			person_dict["Designation"] = staff.person_desig
			person_dict["Needs Accomodation"] = "No"
			person_dict["LivingSpace"] = "None"
			person_dict["Office"] = "X" #To allocate randomly
		elif person_des == "F":
			fellow = Fellow()
			person_dict["Name"] = person_name
			person_dict["Designation"] = fellow.person_desig

	def reallocate_person(self):
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
ed.create_room("Kked", "O")