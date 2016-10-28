"""Amity Allocator
This app enables allocation of offices and living spaces at Amity

Usage:
	amity create_room <name> <room_type>
	amity add_person <name> <designation> <needs_acc>
	amity reallocate_person <name> <room_type> <new_room>
	amity remove_person <name>
	amity print_room <name>
	amity print_allocations [-o=filename]
	amity print_unallocated [-o=filename]
	amity load_people <filename>
	amity load_state <dbname>
	amity save_state [--db=dbname]
	amity -i|--interactive
	amity -h|--help
	amity -v|--version

Options:
	-o		outputs the results to a file
	--db 	specifies the database to read from or write to
	-h|--help displays help message
	-i|--interactive opens the app in interactive mode
"""
import cmd
import os
import sys

#from colorama import init
from docopt import docopt, DocoptExit
from termcolor import cprint
from pyfiglet import figlet_format

import amity
from amity import Amity


def app_exec(func):
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			print('Invalid command')
			print(e)
		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)

	return fn

class Allocator(cmd.Cmd):
	intro = cprint(figlet_format("Amity Room Allocator", font="bulbhead"), "yellow")
	prompt = "Amity>> "

	@app_exec
	def do_create_room(self, args):
		"""Creates new rooms

		Usage: create_room <name> <room_type>
		"""
		Amity.create_room(args["<name>"], args["<room_type>"])
	


if __name__ == '__main__':
	Allocator().cmdloop()
