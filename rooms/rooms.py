class Room(object):
    """Super class for rooms."""
    def __init__(self, r_name, r_type=None, capacity=None):
        self.r_name = r_name
        self.r_type = r_type
        self.capacity = capacity
        self.occupants = 0


class Office(Room):
    def __init__(self, r_name):
        super(Office, self).__init__(r_name, r_type="OFFICE", capacity=6)


class LivingSpace(Room):
    def __init__(self, r_name):
        super(LivingSpace, self).__init__(r_name, r_type="LIVINGSPACE",
                                          capacity=4)
