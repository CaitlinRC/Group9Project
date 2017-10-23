from map import rooms
from items import *
from player import *
from gameparser import *

# Work that still needs to be done:
# Sort Interactions function (mummy/cowboy/hades etc)
# Needs to print what you can take/drop/use in a room + current lives
# Need print room items/print inventory functions

# Extra stuff:
# Title screen?
# ASCII art?
# Background music?

======
def print_room(room):
	"""This function displays current room's name and description. Also, if there are any items, it displays them"""
	print(room["name"].upper())
	print()
	print(room["description"])
	print()
	print()
	print_room_items(room)

		
=======

# main/menu to run the whole thing

def use(user_input):

    global inventory

    if (user_input == 'sword') and (item_sword in inventory):

        choice = input('Use on what: ')

        if (choice == 'ore') and (item_ore in inventory):

            print('You cut open the ore and retrieve the precious metal from inside it. \nThe rest of the ore crumbles in your hand and dulls your sword - rendering it useless. \nYou leave it behind.')

            inventory.remove(item_ore)
            inventory.remove(item_sword)
            inventory.append(item_metal)

        else:
            print('The sword can\'t be used on that.')

    elif (user_input == 'armour') and (item_armour in inventory):

        print('You put on the armour, the heavy metal weighing you down but protecting you from any harm.')
        item_armour["worn"] = True
        inventory.remove(item_armour)

    else:
        print('You cannot use that.')
      

=======
def take(item_id):
        """This function takes an item_id and moves it from the list of items in the current room to the player's inventory."""   
    item_exists = False
    for item in current_room["items"]:
        if item_id == item["id"]:
            item_exists = True
            current_room["items"].remove(item)
            inventory.append(item)
            print(item["name"] + " added to your bag")
        if not item_exists:
            print("You cannot take that")


=======
def drop(item_id):
	for item in inventory:
		if item["id"] == item_id:
			inventory.remove(item)
			current_room["items"].append(item)
			print("You have dropped", (item["name"]), "in", (current_room["name"]), ".")
			break
		else:
			print("You cannot drop item here.")
			      
			      
=======
def print_menu(exits, room_items, inv_items):
        print("You can:")
        for direction in exits:
                print_exit(direction, exit_leads_to(exits, direction))   
        print("What do you want to do?")

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:"""

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
"""
    print("GO " + direction.upper() + " to " + leads_to + ".")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:"""

    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    exits = current_room['exits']

    if is_valid_exit(exits, direction):
        current_room = move(exits, direction)

    else:
        print("You cannot go through that portal.")


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:"""

    # Next room to go to
    return rooms[exits[direction]]

def main():

    # Main game loop
    while True:
       
        
        print_room(current_room)
        print_inventory_items(inventory)

       
        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

if __name__ == "__main__":
    main()
