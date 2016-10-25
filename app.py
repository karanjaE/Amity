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

from docopt import docopt, DocoptExit

import amity
from amity import Amity

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format("Amity Room Allocator", font="bulbhead"),
	"yellow")