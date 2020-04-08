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

game = True

# Make a new player object that is currently in the 'outside' room.
player1 = Player("KingLouie", room["outside"])
options = ["n", "e", "s", "w", "q"]

# Write a loop that:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

while game:
    print(player1.current_room)
    user = input("In which direction do you want to go?\n\n[n] North [e] East [s] South [w] West [q] Quit\n\n")
    if user == "q":
        print("\nWe hope you had fun\n")
        game = False    
    elif user not in options:
        print("Please choose one of the directions or quit the game\n")
    else: 
        user += "_to"
        if getattr(player1.current_room, user) == None:
            print("\nThere is no room where you want to go\nPlease choose another direction!")
        else:
            player1.current_room = getattr(player1.current_room, user)    
    