from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Backpack', 'Empty and tattered but maybe it can be useful in the cave'), Item('Lamp', 'Shattered but maybe it can be rapaired with some tools')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player1 = Player("KingLouie", room["outside"])
game = True
options1 = ["n", "e", "s", "w"]
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.


while game:
    
    print(player1.current_room)
    print(player1)

    action = input("\nWhat do you want to do now? - [move] to move [take] to take an item \n[drop] to drop an item [i] to see your inventory [q] to quit game\n\n")
    if action == "q":
            print("\nWe hope you had fun\n")
            game = False
    elif action == "take":
        if len(player1.current_room.items) == 0:
            print("\n***There are no items in the room you can take***")
        else:
            item_to_take = input("\nWhich item do you want to take?\n")
        for e in player1.current_room.items:
            if item_to_take == e.name:
                setattr(player1, "inventory", [*player1.inventory, e])
                player1.current_room.items.remove(e)
                e.took_item()
    elif action == "drop":
        if len(player1.inventory) == 0:
            print("\n***Your inventory is empty - you can't drop an item***")
        else:
            item_to_drop = input("\nWhich item do you want to drop?\n")
        for e in player1.inventory:
            if item_to_drop == e.name:
                setattr(player1.current_room, "items", [*player1.current_room.items, e])
                player1.inventory.remove(e)
                e.dropped_item()
    elif action == "move":
        move = input("\nIn which direction do you want to go? - [n] North [e] East [s] South [w] West\n\n")
        if move not in options1:
            print("\nPlease choose one of the directions\n")
        else: 
            move += "_to"
            if getattr(player1.current_room, move) == None:
                print("\n***There is no room where you want to go - Please choose another direction***")
            else:
                player1.current_room = getattr(player1.current_room, move)    
    elif action == "i":
        if len(player1.inventory) == 0:
            print("\n***Your inventory is empty***")
        else:
            player1.show_inv()
    else:
        print("\n***Please choose between the possible options or quit the game***") 