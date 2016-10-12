# from amity.amity import Amity

rooms_list = []
class Room(object):
	"""Super class for rooms. Defines methods that affect
	both office	and living space classes.
	"""
	def __init__(self, r_type=None, capacity=None):
		self.r_type = r_type
		self.capacity = capacity

	def create_room(self,room_name):
		room_dict = dict()
		room_dict["Name"] = room_name
		room_dict["Type"] = self.r_type
		room_dict["Capacity"] = self.capacity

		rooms_list.append(room_dict)
		# rooms_list.append(room_name)

	def print_allocations(self):
		"""Prints all rooms and all the people that have been allocated 
		those rooms
		"""
		pass

	def print_unallocated(self):
		pass


class Office(Room):
	"""Performs tasks unique to offices
	"""
	def __init__(self):
		super(Office, self).__init__(r_type="OFFICE", capacity=6)

class LivingSpace(Room):
	"""Docstring
	"""
	def __init__(self):
		super(LivingSpace, self).__init__(r_type="LIVINGSPACE", capacity=4)





l = LivingSpace()
l.create_room('Krypton')


s = Office()
s.create_room('Shannara')

print(rooms_list)
