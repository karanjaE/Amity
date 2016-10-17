class Person(object):
    def __init__(self, name, designation=None, needs_acc="N"):
        self.name = name
        self.designation = designation
        # self.office = office
        self.needs_acc = needs_acc

class Fellow(Person):
    def __init__(self):
        super(Fellow, self).__init__(designation="FELLOW")

class Staff(Person):
    def __init__(self):
        super(Staff, self).__init__(designation="STAFF")
