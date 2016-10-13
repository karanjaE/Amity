class Person(object):
	"""Docstring
	"""
	def __init__(self, person_desig=None, needs_acc="N"):
		self.person_desig = person_desig
		self.needs_acc = needs_acc


class Staff(Person):
	def __init__(self):
		super(Staff, self).__init__(person_desig="STAFF")

class Fellow(Person):
	def __init__(self):
		super(Fellow, self).__init__(person_desig="FELLOW")