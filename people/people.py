import random

# from rooms import rooms

offices = ["Home", "Vale"]
l_spaces = []
people_list = []

class Person(object):
	"""Docstring
	"""

	def __init__(self, p_type=None, needs_acc=None, l_space=None, office=None):
		"""Docstring
		"""
		# self.p_type = p_type
		self.p_type = p_type
		self.needs_acc = needs_acc
		self.l_space = None
		self.office = None

	def add_person(self, p_name):
		person_dets = dict()
		person_dets["Name"] = p_name
		person_dets["Designation"] = self.p_type
		person_dets["Needs Acommodation"] = self.needs_acc
		
		if self.p_type == "STAFF":
			self.needs_acc = "N"
			self.l_space = None
			self.office = "" #Allocate office randomly
		elif self.p_type == "FELLOW":
			self.office = ""#Allocate office randomly
			

		people_list.append(person_dets)
		return


class Fellow(Person):
	"""Docstring
	"""
	super(Fellow, self).__init__(p_type="FELLOW", )


p = Person()
print(p.p_type)
