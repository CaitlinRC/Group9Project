# Interactions with Characters

# Interactions To Do:
# Hades

from map import rooms
from items import *
from player import *
from gameparser import *
from game import *


def cowboy_interaction():
    
    global lives
    global inventory
    global current_room
    
    print('The cowboy steps in front of you and glares at you. He says: \n"Look buddy. We don\'t take kindly to strangers here. So take your fancy clothes and leave before this gets ugly."')

    while True:

        user_input = input('\nYou can: TALK to him, PUNCH him or KISS him (because why not).')

        filtered_input = normalise_input(user_input)

        if filtered_input[0] == 'talk':

            print('He doesn\'t appreciate you trying to smart talk him. Before you can get a word out, he punches you in the face (-1 Life).')
            lives -= 1

        elif filtered_input[0] == 'punch':

            print("You land a solid hit on the bridge of his nose and he staggers backwards, tripping over his chair and landing on his ass.\nHe and his friends back away from you. You snatch up the bottle of whiskey from the table.")
            inventory.append(item_whiskey)
            current_room["items"].remove(item_whiskey)
            False

        elif filtered_input[0] == 'kiss':

            print("For whatever reason, you decide to kiss him. He pushes you off him, wiping his mouth and says: 'Sorry buddy, you ain't my type.'")
            
        else:
            print("You can\'t do that.")
            
def mummy_interaction():

    global lives
    global inventory
    global current_room

    print('As you step closer to the sarcophagus, a mummy rises from it and staggers towards you.\nIt\'s teeth are gnashing for a taste of your skin. You can see the gems you need glinting behind it.')

    while True:
        
        user_input = input('\nYou can: Attempt to TAKE the gem, GO SOUTH to the previous room or attempt to FIGHT: ')

        filtered_input = normalise_input(user_input)
        print(filtered_input)

        if filtered_input[0] == 'fight':

            print('You attempt to attack the mummy, flailing at it with your weapons. They have no effect.\nThe mummy clearly doesn\'t feel pain and continues to sink its teeth into your skin. (-1 Life)')
            lives -= 1

        elif (filtered_input[0] == 'take') and (filtered_input[1] == 'gem'):

            if item_armour["worn"] == True:

                print('You grab the gem, the mummys teeth unable to harm you in your suit of armour.')
                inventory.append(item_gem)
                False

            else:
                print('The mummy\'s teeth sink into your skin! If only you had some protection... (-1 Life)')
                lives -= 1

        elif (filtered_input[0] == 'go') and (filtered_input[1] == 'south'):

            exits = current_room["exits"]
            current_room = move(exits, "south")
            # THIS BIT DOESNT WORK YET BUT IT DOES RUN WHEN NEEDED
            False

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

        if user_input == 'nothing':

            print("Poseidon stares at you in shock for a moment before handing over his trident and storming off in a huff.")
            inventory.append(item_trident)
            current_room["items"].remove(item_trident)
            False

        else:
            print("Incorrect! As a punishment, Poseidon smites you. (-1 Life)")
            lives -= 1
        
    

def hades_interaction():

    global lives
    global current_room
    global inventory

    print('Hades speaks to you, his demonic voice sending shivers down your spine:\n"So mortal, you come seeking your possessions back? Well, I\'ll give it to you if you give me my brother\'s toy."')

    while True:

        user_input = input("Your options are: DROP Trident, GO SOUTH back to the Underworld.")

        filtered_input = normalise_input(user_input)

        if (filtered_input[0] == "drop") and (filtered_input[1] == "trident"):

            inventory.remove(item_trident)
            inventory.append(item_keys)

            print("Hades chucks you the set of keys and gestures for you to get out, too focused on the trident to care about you anymore.")

            exits = current_room["exits"]
            current_room = move(exits, "south")
            False

        elif (filtered_input[0] == "go") and (filtered_input[1] == "south"):

            exits = current_room["exits"]
            current_room = move(exits, "south")
            False

        else:
            print("You can\'t do that.")
            
def guard_interaction():

    print("If you want to enter Hade\'s dwelling, you must be able to be able to handle the heat. (Need at least 2 lives)\nHe has something of yours that fell from the sky, maybe if you give him his brother's weapon then you can strike a deal...")
