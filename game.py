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
# Display Room (Description/Items/Options)
# Something to deal with Speech (??)

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
			      
			      
