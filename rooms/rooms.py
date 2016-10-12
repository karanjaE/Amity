from amity.amity import Amity

offices = []
living_spaces = []


class Room(Amity):
	"""Super class for rooms. Defines methods that affect
	both office	and living space classes.
	"""
	def __init__(self, name):
		self.name = name
		if not self.name.isalpha():
			return("Error. Name can only contains alphabets")		

	def print_allocations(self):
		#return all the allocations; ie all rooms and people
		#in them.
		pass

	def print_room(self):
		pass
		