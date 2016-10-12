from rooms import rooms

class Office(rooms.Room):
	"""performs functionality unique to office
	"""

	def create_room(self):
		room_dict = dict()
		room_dict["name"] = self.name
		room_dict["type"] = "office"
		room_dict["capacity"] = 6

		rooms.offices.append(room_dict)