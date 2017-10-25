from map import rooms
from items import *
from player import *
from gameparser import *
import time
import pygame


# INTERACTIONS CODE

def cowboy_interaction():
    
    global lives
    global inventory
    global current_room
    
    print('The cowboy steps in front of you and glares at you. He says: \n"Look buddy. We don\'t take kindly to strangers here. So take your fancy clothes and leave before this gets ugly."')

    while True:

        user_input = input('\nYou can: \n\n1)TALK to him \n2)PUNCH him  \n3)KISS him (because why not) \n\nWhat do you do: ')

        filtered_input = normalise_input(user_input)

        if filtered_input == []:

            print('Please enter a valid option: ')

        elif filtered_input[0] == 'talk':

            print('\nHe doesn\'t appreciate you trying to smart talk him. Before you can get a word out, he punches you in the face (-1 Life).')
            lives -= 1

            if lives <= 0:
                print("You are out of lives and have lost the game. Guess you will never get home...")
                time.sleep(5)
                quit()

        elif filtered_input[0] == 'punch':

            print("\nYou land a solid hit on the bridge of his nose and he staggers backwards, tripping over his chair and landing on his ass.\nHe and his friends back away from you. You snatch up the bottle of whiskey from the table.")
            inventory.append(item_whiskey)
            current_room["interaction"] = False
            break

        elif filtered_input[0] == 'kiss':

            print("\nFor whatever reason, you decide to kiss him. He pushes you off him, wiping his mouth and says: 'Sorry buddy, you ain't my type.'")
            
        else:
            print("\nYou can\'t do that.")
            
def mummy_interaction():

    global lives
    global inventory
    global current_room

    leaving_interaction = False

    print('As you step closer to the sarcophagus, a mummy rises from it and staggers towards you.\nIt\'s teeth are gnashing for a taste of your skin. You can see the gems you need glinting behind it.')

    while True:
        
        user_input = input('\nYou can: Attempt to TAKE the gem, GO SOUTH to the previous room or attempt to FIGHT: ')

        filtered_input = normalise_input(user_input)

        if filtered_input == []:

            print('Please enter a valid option: ')

        elif filtered_input[0] == 'fight':

            print('You attempt to attack the mummy, flailing at it with your weapons. They have no effect.\nThe mummy clearly doesn\'t feel pain and continues to sink its teeth into your skin. (-1 Life)')
            lives -= 1

            if lives <= 0:
                print("You are out of lives and have lost the game. Guess you will never get home...")
                time.sleep(5)
                quit()

        elif (filtered_input[0] == 'take') and (filtered_input[1] == 'gem'):

            if item_armour["worn"] == True:

                print('You grab the gem, the mummys teeth unable to harm you in your suit of armour.')
                inventory.append(item_gem)
                current_room["interaction"] = False
                break

            else:
                print('The mummy\'s teeth sink into your skin! If only you had some protection... (-1 Life)')
                lives -= 1

                if lives <= 0:
                    print("You are out of lives and have lost the game. Guess you will never get home...")
                    time.sleep(5)
                    quit()

        elif (filtered_input[0] == 'go') and (filtered_input[1] == 'south'):

            exits = current_room["exits"]
            current_room = move(exits, "south")
            print_room(current_room)
            break

        else:
            print('You cannot do that.')

    

def poseidon_interaction():

    global inventory
    global current_room
    global lives

    print("Hello there mortal. I presume you are after the trident? Ha!\nYou know what, since I'm feeling generous - if you solve my riddle, you can have it.")

    while True:
        print("\nPoor people have it, rich people need it and if you eat it, you will die.")

        user_input = input("What is it? ")
        filtered_input = normalise_input(user_input)
        
        if filtered_input[0] == 'nothing':

            print("\nPoseidon stares at you in shock for a moment before handing over his trident and storming off in a huff.")
            inventory.append(item_trident)
            current_room["interaction"] = False
            break

        else:
            print("\nIncorrect! As a punishment, Poseidon smites you. (-1 Life)")
            lives -= 1

            if lives <= 0:
                print("You are out of lives and have lost the game. Guess you will never get home...")
                time.sleep(5)
                quit()
        
    

def hades_interaction():

    global lives
    global current_room
    global inventory

    
    print("The lava burns your feet. (-1 Life)")
    lives -= 1

    if lives <= 0:
        print("You are out of lives and have lost the game. Guess you will never get home...")
        time.sleep(5)
        quit()
        
    print('Hades speaks to you, his demonic voice sending shivers down your spine:\n"So mortal, you come seeking your possessions back? Well, I\'ll give it to you if you give me my brother\'s toy."')

    while True:

        user_input = input("Your options are: DROP Trident, GO SOUTH back to the Underworld: ")

        filtered_input = normalise_input(user_input)

        if filtered_input == []:

            print('Please enter a valid option: ')

        elif (filtered_input[0] == "drop") and (filtered_input[1] == "trident"):

            inventory.remove(item_trident)
            inventory.append(item_keys)

            print("\nHades chucks you the set of keys and gestures for you to get out, too focused on the trident to care about you anymore.")

            current_room["interaction"] = False
            exits = current_room["exits"]
            current_room = move(exits, "south")
            print_room(current_room)
            break

        elif (filtered_input[0] == "go") and (filtered_input[1] == "south"):

            exits = current_room["exits"]
            current_room = move(exits, "south")
            print_room(current_room)
            break

        else:
            print("You can\'t do that.")
            
def guard_interaction():

    print("If you want to enter Hade\'s dwelling, you must be able to be able to handle the heat. (Need at least 2 lives)\nHe has something of yours that fell from the sky, maybe if you give him his brother's weapon then you can strike a deal...")

# END OF INTERACTIONS CODE

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
#"""This function displays current room's name and description. Also, if there are any items, it displays them"""
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print()
    print_room_items(room)


# main/menu to run the whole thing

def use(item_id):

    global inventory

    if (item_id == 'sword') and (item_sword in inventory):

        choice = input('Use on what: ')

        if (choice == 'ore') and (item_ore in inventory):

            print('You cut open the ore and retrieve the precious metal from inside it. \nThe rest of the ore crumbles in your hand and dulls your sword - rendering it useless. \nYou leave it behind.')

            inventory.remove(item_ore)
            inventory.remove(item_sword)
            inventory.append(item_metal)

        else:

            if item_ore not in inventory:
                print('You can\'t cut something you don\'t have!')

            else:
                print('The sword can\'t be used on that.')

    elif (item_id == 'armour') and (item_armour in inventory):

        print('You put on the armour, the heavy metal weighing you down but protecting you from any harm.')
        item_armour["worn"] = True
        inventory.remove(item_armour)

    else:
        print('You cannot use that.')
      

def take(item_id):
#"""This function takes an item_id and moves it from the list of items in the current room to the player's inventory."""  
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

    global current_room

    if current_room["interaction"] == True:

        if current_room["name"] == "Saloon":

            cowboy_interaction()

        elif current_room["name"] == "Atlantis":

            poseidon_interaction()

        elif current_room["name"] == "Egypt":

            mummy_interaction()

        elif current_room["name"] == "Underworld":

            guard_interaction()

        elif current_room["name"] == "Boss":

            hades_interaction()
 
    
    print("\nYou can:\n")
    
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")

    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")

        if (item["id"] == "sword") or (item["id"] == "armour"):
            print("USE " + item["id"].upper() + " to use " + item["name"] + ".")
        
    print("\nWhat do you want to do?")


def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":

        if len(command) > 1:
            use(command[1])

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
    this exit leads."""

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
    # init music
        pygame.mixer.init()
        # load music
        track = pygame.mixer.music.load(current_room["bgm"])
        # set volume
        pygame.mixer.music.set_volume(5.0)
        # play music
        pygame.mixer.music.play()
        # Main game loop

    else:
        print("You cannot go through that portal.")


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:"""

    # Next room to go to
    return rooms[exits[direction]]


def main():
   
    print("")
    print("")
    print("")
    print("██████╗  ██████╗ ██████╗ ████████╗ █████╗ ██╗     ")
    print("██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ")
    print("██████╔╝██║   ██║██████╔╝   ██║   ███████║██║     ")
    print("██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██║██║     ")
    print("██║     ╚██████╔╝██║  ██║   ██║   ██║  ██║███████╗")
    print("╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝")
    print("                      ██╗██╗   ██╗███╗   ███╗██████╗ ")
    print("                      ██║██║   ██║████╗ ████║██╔══██╗")
    print("                      ██║██║   ██║██╔████╔██║██████╔╝")
    print("                 ██   ██║██║   ██║██║╚██╔╝██║██╔═══╝ ")
    print("                 ╚█████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ")
    print("                  ╚════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝   ")
    print()
    print("                    oooooOOOOOOOOOOOOOOOOooooo ")
    print("                  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ")
    print("                 IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII ")
    print("                HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH ")
    print("               zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz ")
    print("    .<><><><><><><><><><><><><><><><><><><><><><><><><><><><>. ")
    print("  /XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\ ")
    print("/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\ ")
    print("\XXX[  ]XXX[  ]XXXX[  ]XXXX[  ]XXXX[  ]XXXX[  ]XXXX[  ]XXX[  ]XXX/ ")
    print("  \XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ ")
    print("      ~~~~\XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/~~~~ ")
    print("               /   ~~~<><><><><><><><><><>~~~   \ ")
    print("              /      /       |   |        \      \ ")
    print("             /     /               |        \     \ ")
    print("            /    /           |                \    \ ")
    print("           /   /               |   |            \   \ ")
    print("          /  /               |                    \  \ ")
    print("        _/_/                     | |                \_\_ ")
    time.sleep(2)

    print("""A long time ago in a galaxy far, far away…

After a long, tedious journey through both galaxies and new dimensions you 
find yourself at the mercy of a blackhole, with barely any fuel, a broken 
battery, and no defence shield, disaster strikes. A rogue asteroid hits
your spaceship ripping a hole into the power room of your ship, before you
can engage the cockpit oxygen locks, your last fuel can, battery ore, tools
and parachute are sucked out into the hole.

After securing the cockpit, you realise that you will not have enough fuel
to get you home, nor will your generator battery last. Your only option is
to land on the nearest planet. After a bumpy ride through Pandora’s atmosphere
you make a crash landing on the outskirts of a town. You realise your only hope
of getting home is to hunt down the necessary parts to fix your spaceship.

You reach the local “repair shop” and enter through the front door.""")

    
    win = False
    while not (win):
       
        print_room(current_room)
        print_inventory_items(inventory)

        command = menu(current_room["exits"], current_room["items"], inventory)

        execute_command(command)

        if (item_gem in rooms["Repair"]["items"]) and (item_keys in rooms["Repair"]["items"]) and (item_metal in rooms["Repair"]["items"]) and (item_whiskey in rooms["Repair"]["items"]):
            win = True
            print("\nCONGRATULATIONS YOU HAVE WON. YOU FLY HOME TO EARTH, READY FOR ANOTHER ADVENTURE!")
            time.sleep(5)
            break


if __name__ == "__main__":
    main()
