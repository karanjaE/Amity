#!/usr/bin/env python
"""
Amity Allocator
This system makes it easy to manage rooms and people at Amity.
Usage:
	create_room <room_type> <room_name>
	add_person <first_name> <last_name> <designation> [--needs_accomodation=N]
	reallocate_person <person_id> <room_type> <new_room>
	load_people <filename>
	print_room <room_name>
	print_allocations [--o=filename]
	print_unallocated [--o=filename]
	load_state [--dbname]
	save_state [--o=db_name]
	quit
	(-i | --interactive)
Options:
	-h --help Show this screen.
	-i --interactive Interactive mode.
	-v --version
"""
import cmd

from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint

from amity import Amity


def app_exec(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid command! See help."
			print(msg)
			print(e)
			return

		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)

	return fn


class AmityApp(cmd.Cmd):
	intro = cprint(figlet_format("Amity Room Allocator", font="bulbhead"),\
				"yellow")
	prompt = "Amity --> "

	@app_exec
	def do_create_room(self, arg):
		"""Creates a new room
		Usage: create_room <room_type> <room_name>...
		"""
		names = arg["<room_name>"]
		rtype = arg["<room_type>"]
		if not len(names) or not rtype:
			print("Make sure you enter all details")
		elif rtype.upper() not in ["L", "O"]:
			print("Invalid room type entered. Use either O or L")
		else:
			for name in names:
				if not name.isalpha():
					print("Room name can only contain alphabets. Try again")
				Amity.create_room(rtype, name)

	@app_exec
	def do_add_person(self, arg):
		"""
		Adds a person and allocates rooms if available
		Usage: add_person <first_name> <last_name> <designation> [--needs_accomodation=N]
		"""
		fname = arg["<first_name>"]
		lname = arg["<last_name>"]
		designation = arg["<designation>"]
		needs_accomodation = arg["--needs_accomodation"]
		if not fname.isalpha() or not lname.isalpha():
			print("Names can only contain alphabets.")
		elif designation.upper() not in ["F", "S"]:
			print("Invalid designation. Enter F or S")
		elif needs_accomodation.upper() not in ["Y", "N"]:
			print("Invalid accomodation option. Enter Y or N")
		elif designation.upper() == "S" and needs_accomodation.upper() == "Y":
			print("Staff cannot get accomodation!")
		else:
			if not needs_accomodation:
				needs_accomodation = "N"
			Amity.add_person(fname,lname, designation, needs_accomodation)
			print(fname.upper() + " " + lname.upper() + "added.")

	@app_exec
	def do_print_room(self, arg):
		"""
		Prints all the people in a given rooms
		Usage: print_room <room_name>
		"""
		Amity.print_room(arg["<room_name>"])

	@app_exec
	def do_print_allocations(self, arg):
		"""
		Prints all rooms and the people in them.
		Usage: print_allocations [--o=filename]
		"""
		filename = arg["--o"] or ""
		Amity.print_allocations(filename)

	@app_exec
	def do_print_unallocated(self, arg):
		"""
		Prints all the people that don't have relevant rooms
		Usage: print_unallocated [--o=filename]
		"""
		filename = arg["--o"] or ""
		Amity.print_unallocated(filename)

	@app_exec
	def do_load_people(self, arg):
		"""
		Loads people from a text file to the app.
		Usage: load_people <filename>
		"""
		Amity.load_people(arg["<filename>"])
		print("File loaded.")

	@app_exec
	def do_reallocate_person(self, arg):
		"""
		Reallocates person
		Usage: reallocate_person <full_name> <room_type> <new_room>
		"""
		full_name = arg["<full_name>"]
		rtype = arg["<room_type>"]
		nroom = arg["<new_room>"]
		Amity.reallocate_person(full_name, rtype, nroom)

	@app_exec
	def do_load_state(self, arg):
		"""
		Loads data from the specified db into the app.
		Usage: load_state <filename>
		"""
		Amity.load_state(arg["<filename>"])

	@app_exec
	def do_save_state(self, arg):
		"""
		Persists app data into the given db
		Usage: save_state [--db_name=sqlite_db]
		"""
		db = arg['--db_name']
		if db:
			Amity.save_state(db)
		else:
			Amity.save_state()

	@app_exec
	def do_quit(self, arg):
		"""
		Exits the app.
		Usage: quit
		"""
		exit()

if __name__ == '__main__':
	AmityApp().cmdloop()
