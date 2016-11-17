[![Codacy Badge](https://api.codacy.com/project/badge/Grade/77d1b2d24edc49ce91f480998d73bafa)](https://www.codacy.com/app/edward-karanja/Amity?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-ekaranja/Amity&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/andela-ekaranja/Amity.svg?branch=ft-db-integration)](https://travis-ci.org/andela-ekaranja/Amity)
[![Coverage Status](https://coveralls.io/repos/github/andela-ekaranja/Amity/badge.svg?branch=master)](https://coveralls.io/github/andela-ekaranja/Amity?branch=master)

# AMITY ALLOCATOR
### Intro
Amity Allocator is a CLI based Python app that enables creation of rooms, addition of people into the system and their reallocation to various rooms as need arises.
### System requirements
- Python version 3.5 +
- Python virtialenv
- SQLite3

### Setup
- `git@github.com:andela-ekaranja/Amity.git` for SSH or `https://github.com/andela-ekaranja/Amity.git` for HTTPS.
- Create a virtualenv and activate it.
- In your shell, `cd` into the app root and run `pip install -r requirements.txt`
- To start the app run `python -i app.py`

### Usage
- `create_room <room_type> <room_name>` : Creates a new room
- `add_person <first_name> <last_name> <designation> [<needs_accomodation>]` : Adds a new person and allocates them a random room.
- `print_room <room_name>`: Prints all the members of the specified room.
- `reallocate_person <name> <new_room>`: Moves a person from one room to another.
- `load_people <filename>`: Does batch addition of people using data from a `filename.txt`
- `print_allocations [<filename>]`: Prints all rooms and the people in them and optionally writes the data to `filename.txt`.
- `print_unallocated [<filename>]`: Prints all the people that haven't been allocated and optionally writes the data to `filename.txt`.
- `load_state [<filename>]`: Loads data from the specified SQLite db into the app
- `save_state [<db_name>]`: Persists data stored in the app to a SQLite DB
- `(-i | --interactive)`
- 	`-h --help Show this screen.`:  Shows help text
-	`-i --interactive Interactive mode.` Starts the app in interactive mode

### Tests
To run tests, run `nosetests` or `nosetests --with-coverage`

### Contributing
The app is free and open for anyone that feels they have features they can add or change. Just fork and start contributing.

Released under the [MIT lisence](https://opensource.org/licenses/MIT).
