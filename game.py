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

<<<<<<< HEAD
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


    else:
        print('You cannot use that.')
        
>>>>>>> e98aa971edcd676841c51b0d1417192e912f011f
