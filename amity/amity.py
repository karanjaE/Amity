class Amity(object):
	"""Super class from which all other classes inherit.
	Contains functionality such as:
	load_state() which loads data from a db into the app
	save_state() which loads data stored in the app into a db
	"""
	def load_state(self):
		'''write func to load data from a db into the app
		'''
		pass

	def save_state(self):
		'''Write func to save app data to a db
		'''
		pass 