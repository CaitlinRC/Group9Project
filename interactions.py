# Interactions with Characters

# Interactions To Do:
# Cowboy
# Mummy
# Poseidon
# Hades
# Guard

from map import rooms
from items import *
from player import *
from gameparser import *
from character_dict import *
from game import *


def cowboy_interaction():

    pass

def mummy_interaction():

    global lives

    print('As you step closer to the sarcophagus, a mummy rises from it and staggers towards you.\nIt\'s teeth are gnashing for a taste of your skin. You can see the gems you need glinting behind it.')

    while True:
        
        user_input = input('\nYou can: Attempt to TAKE the gem, GO SOUTH to the previous room or attempt to FIGHT: ')

        filtered_input = normalise_input(user_input)

        if (len(filtered_input) == 1) and (filtered_input[0] == 'fight'):

            print('You attempt to attack the mummy, flailing at it with your weapons. They have no effect.\nThe mummy clearly doesn\'t feel pain and continues to sink its teeth into your skin. (-1 Life)')
            lives -= 1

        elif (filtered_input[0] == 'take') and (filtered_input[1] == 'gem'):

            if item_armour["worn"] == True:

                print('You grab the gem, the mummys teeth unable to harm you in your suit of armour.')
                False

            else:
                print('The mummy\'s teeth sink into your skin! If only you had some protection... (-1 Life)')
                lives -= 1

        elif (filtered_input[0] == 'go') and (filtered_input[1] == 'south'):

            execute_go("south")
            False

        else:
            print('You cannot do that.')

    

        
        
    print(lives)

def poseidon_interaction():

    pass

def hades_interaction():

    pass

def guard_interaction():

    print(character["guard"])

mummy_interaction()
