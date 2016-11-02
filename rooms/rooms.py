class Room(object):
    """Super class for rooms. Defines methods that affect
	both office	and living space classes.
	"""
    def __init__(self, r_name, r_type=None, capacity=None):
        self.r_name = r_name
        self.r_type = r_type
        self.capacity = capacity


class Office(Room):
    def __init__(self):
        super(Office, self).__init__(r_type="OFFICE", capacity=6)


class LivingSpace(Room):
    def __init__(self):
        super(LivingSpace, self).__init__(r_type="LIVINGSPACE", capacity=4)
