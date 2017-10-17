# Map File for Group Project Game

# Repair Room, Saloon, Spaceship, Medieval, Underworld, Atlantis, Egypt, Boss Room

repair_room = {"name": "Repair Shop", "description": "isahd", "exits": {"north": "Saloon"}, "items": []}

saloon_room = {"name": "Saloon", "description": "suihdiuh", "exits": {"south": "Repair", "north": "Atlantis", "west": "Castle"}, "items": [item_whiskey]}

atlantis_room = {"name": "Atlantis", "description": "ajsdh", "exits": {"south": "Saloon", "north": "Space"}, "items": [item_trident]}

medieval_room = {"name": "Castle", "description": "uisdh", "exits": {"east": "Saloon", "north": "Egypt"}, "items": [item_sword, item_armour]}

egypt_room = {"name": "Egypt", "description": "spooky", "exits": {"south": "Medieval", "east": "Space"}, "items": [item_gem]}

space_room = {"name": "Space", "description": "woo", "exits": {"west": "Egypt", "south": "Atlantis", "north": "Underworld"}, "items": [item_ore]}

underworld_room = {"name": "Underworld", "description": "spppppp", "exits": {"south": "Space", "north": "Boss"}, "items": []}

boss_room = {"name": "Boss", "description": "muahahahha", "exits": {"south": "Underworld"}, "items": [item_keys]}
