from rooms import rooms

class LivingSpace(rooms.Room):
	"""Performs functionality unique to living spaces
	"""
	# def __init__(self):
	# 	self.room_type = "living space"

	def create_room(self):
		room_dict = dict()	
		room_dict["name"] = self.name
		room_dict["type"] = "living space"
		room_dict["capacity"] = 4

		rooms.living_spaces.append(room_dict)
