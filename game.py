# Main Game File

from map import rooms
from items import *
from player import *
from gameparser import *

# Functions Needed:
# Move
# Take
# Drop
# Use
# Something to deal with Speech (??)

def print_room(room):
	"""This function displays current room's name and description. Also, if there are any items, it displays them"""
	print(room["name"].upper())
	print()
	print(room["description"])
	print()
	print()
	print_room_items(room)

		