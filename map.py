# Map File for Group Project Game

from items import *
import pygame

# Repair Room, Saloon, Spaceship, Medieval, Underworld, Atlantis, Egypt, Boss Room
# {Saloon:saloon.mp3, atlantis:underwater.mp3}

repair_room = {"name": "Repair Shop",

               "description": """In the shop you are welcomed by a large pool of oil left on the floor, a rusty
exhaust on the floor and numerous empty cardboard boxes on the floor, the owner
is nowhere to be seen.

You soon realise that your hunt for parts is short lived.
However, in the corner of the shop you notice something glowing under a piece
of crumpled newspaper.

You inspect it from a distance and realise its an intergalactic gun.
Maybe there is some hope of getting home… """,

               "exits": {"north": "Saloon"},

               "items": [],

               "interaction": False,

               "bgm": "empty.wav"

               }

saloon_room = {"name": "Saloon",

               "description": """You are standing in a saloon.
Half a dozen cowboys are sitting down, playing cards and drinking beer.
The bartender stares at you from behind the counter as he polishes a pint glass, various bottles of whiskey and beer stacked behind him.
A rather rugged looking cowboy is staring you down from across the room, with one hand on the top of his gun and the other holding a cigar.
Neither of them look happy to see you.""",

               "exits": {"south": "Repair", "north": "Atlantis", "west": "Castle"},

               "items": [],

               "interaction": True,
               
               "bgm": "saloon.wav"

               }

atlantis_room = {"name": "Atlantis",

                 "description": """You stand in the entrance of Poseidon’s domain, known as Atlantis.
It is a gorgeous palace made of gems and coral, located on the ocean floor.
Chariots ride past you, pulled by sea horses and guards stand between you and the great god Poseidon.
The guards allow you to pass and you stand facing the great god, whose trident glows with mystical power.""",

                 "exits": {"south": "Saloon", "north": "Space"},

                 "items": [],

                 "interaction": True,

                 "bgm": "underwater.wav"                 

                 }

medieval_room = {"name": "Castle",

                "description": """You find yourself in the great hall of a medieval castle.
The walls are covered with tapestries that blaze a family sigil that you are not familiar with.
The room is lined with long benches and tables, clearly several hundred people could fit into this room if it was deemed necessary.
A pair of thrones sit at the far end of the room on a raised platform, with a set of armour standing tall near the door.
In the suit of armour’s hands is a longsword, the metal shining brightly in the light.""",

                 "exits": {"east": "Saloon", "north": "Egypt"},

                 "items": [item_sword, item_armour],

                 "interaction": False,

                 "bgm": "castle.wav"
                 }

egypt_room = {"name": "Egypt",

              "description": """You find yourself standing in one of the Great Pyramids of Ancient Egypt, thousands of years into the past.
Through the dusty air, you can see that the room is filled with countless treasures and priceless artefacts that used to belong to those who were buried here.
In the centre of the room, lies a golden sarcophagus, riddled with gems that look quite like what you need to power your generator…""",

              "exits": {"south": "Castle", "east": "Space"},

              "items": [],

              "interaction": True,

              "bgm": "egypt.wav"
              }

space_room = {"name": "Space",

              "description": """You walk into a cold and empty room, surrounded by metal walls and strange machines with flashing lights.
It is eerily silent, apart from an infrequent beeping noise coming from one of the machines on the wall.
Your eyes drift to the window and you soon realise that you are in an abyss of stars and darkness.
Suddenly, you see a glowing ore in the corner of the room.
Inside, you can see the glint of a precious metal.
This would be perfect to fix your ship’s exhaust with; however, you can’t cut into it with your bare hands.""",

              "exits": {"west": "Egypt", "south": "Atlantis", "north": "Underworld"},

              "items": [item_ore],

              "interaction": False,

              "bgm": "space.wav"
              }

underworld_room = {"name": "Underworld",

                   "description": """You find yourself back in the Underworld.
Around you there are hundreds of lost souls, waiting their turn to cross the river Styx to meet with Hades.
Across the river, you see Cerberus – the monstrous multi-headed dog that stands guard over the realm of the dead.
Your only route to the boss room is by convincing Charon, a man with eyes blazing and an unkempt beard upon his chin, to take you there.""",

                   "exits": {"south": "Space", "north": "Boss"},

                   "items": [],

                   "interaction": True,

                   "bgm": "underworld.wav"
                   }

boss_room = {"name": "Boss",

             "description": """The floor of the room you step into is blazing hot, pools of magma littering the ground.
You follow the winding path, finding yourself before the god of death himself.
Hades stares down at you, curious as to why a mortal such as yourself would bother coming to his domain.
You kneel before him, wary of his power.
In Hades’s hand, is a pair of familiar looking keys – your Hello Kitty keychain swinging ominously back and forth in the god’s hands.""",

             "exits": {"south": "Underworld"},

             "items": [],

             "interaction": True,

             "bgm": "boss.wav"

             }

rooms = {
    "Repair": repair_room,
    "Castle": medieval_room,
    "Saloon": saloon_room,
    "Atlantis": atlantis_room,
    "Egypt": egypt_room,
    "Space": space_room,
    "Underworld": underworld_room,
    "Boss": boss_room
}
