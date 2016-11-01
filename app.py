#!/usr/bin/env python
"""
Amity Allocator
This system makes it easy to manage rooms and people at Amity.
Usage:
	create_room <room_name> <room_type>
	add_person <first_name> <last_name> <designation> [<needs_accomodation>]
	print_room <room_name>
	reallocate_person <name> <room_type> <new_room>
	remove_person <name>
	load_people <filename>
	print_allocations
	print_unallocated
	load_state [<filename>]
	save_state [<db_name>]
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
			msg = "Oops! Invalid command"
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
	prompt = "Amity -->"

	@app_exec
	def do_create_room(self, arg):
		"""
		Creates a new room
		Usage: create_room <room_name> <room_type>
		"""
		try:
			Amity.create_room(arg["<room_name>"], arg["<room_type>"])
		except:
			print("An error occured")

	@app_exec
	def do_add_person(self, arg):
		"""
		Adds a person and allocates rooms if available
		Usage: add_person <first_name> <last_name> <designation> [<needs_accomodation>]
		"""
		try:
			Amity.add_person(arg["<first_name>"], arg["<last_name>"], \
					arg["<designation>"], arg["<needs_accomodation>"])
		except:
			print("An error occured")

	@app_exec
	def do_remove_person(self, arg):
		"""
		Removes person from the system
		Usage: remove_person <name>
		"""
		Amity.remove_person(arg["<name>"])

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
		Usage: print_allocations
		"""
		Amity.print_allocations()

	@app_exec
	def do_print_unallocated(self, arg):
		"""
		Prints all the people that don't have relevant rooms
		Usage: print_unallocated
		"""
		Amity.print_unallocated()

	@app_exec
	def do_load_people(self, arg):
		"""
		Loads people from a text file to the app.
		Usage: load_people <filename>
		"""
		Amity.load_people(arg["<filename>"])

	@app_exec
	def do_load_state(self, arg):
		"""
		Loads data from the specified db into the app.
		Usage: load_state
		"""
		Amity.load_state(arg["<filename>"])

	@app_exec
	def do_save_state(self, arg):
		"""
		Persists app data into the given db
		Usage: save_state [<db_name>]
		"""
		Amity.save_state(arg["<db_name>"])


if __name__ == '__main__':
	AmityApp().cmdloop()
