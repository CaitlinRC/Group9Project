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

def list_of_items(items):
    """This function takes a list of items and returns a comma-separated list of item names."""
    li = ""
    for item in items:
        li = li + ", " + item["name"]
    li = li[2:]
    return li


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room. If there are no items in the room, nothing is printed."""
    if len(list_of_items(room["items"]))!=0:
        print("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items()."""
    if len(items)!=0:
        print("You have " + list_of_items(items) + ".\n")


def print_room(room):
	"""This function displays current room's name and description. Also, if there are any items, it displays them"""
	print(room["name"].upper())
	print()
	print(room["description"])
	print()
	print()
	print_room_items(room)

<<<<<<< HEAD

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


def drop(item_id):
	for item in inventory:
		if item["id"] == item_id:
			inventory.remove(item)
			current_room["items"].append(item)
			print("You have dropped", (item["name"]), "in", (current_room["name"]), ".")
			break
		else:
			print("You cannot drop item here.")
			      
			      
def print_menu(exits, room_items, inv_items):
        print("You can:")
        for direction in exits:
                print_exit(direction, exit_leads_to(exits, direction))   
        print("What do you want to do?")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
=======
		
=======

# main/menu to run the whole thing
>>>>>>> 6f12d9417a7149a8f1d53c0a67ee4c1538e729d2

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then asks the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned."""

    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


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

