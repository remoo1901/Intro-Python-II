from item import Item
from player import Player1
from room import Room
# Declare all the rooms
# Dictionary of rooms mapping name to Room
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
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
room['outside'].items.append(Item("Knife", "Sharp thing"))
room['outside'].items.append(
    Item("Potion", "Green and bubbly liquid in a glass vial"))
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player1 = Player1(room['outside'])
# Write a loop that:
#
while True:
    # * Prints the current room name
    current_room = player1.current_room
    print("player1", player1.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player1.current_room.description)
# * Print items in the room
    print("The room contains the following items:")
    for item in current_room.items:
        print(item)
# * Waits for user input and decides what to do.
    user_input = input(
        "Choose a direction to move in ('n', 's', 'e', 'w') or get or take an item:\n")
# If the user enters a cardinal direction, attempt to move to the room there.
    # moving to a room --> setting current_room on player
    if user_input == "q":
        break
    split_input = user_input.split()
    print(split_input)
    if len(split_input) == 1:
        # move the player
        direction_attribute = f"{user_input}_to"
        if hasattr(current_room, direction_attribute):
            print("Trying to move to: ", getattr(
                current_room, direction_attribute))
            player1.current_room = getattr(current_room, direction_attribute)
        else:
            print("Choose a valid direction to move in")
            continue
    elif len(split_input) == 2:
        item_name = split_input[1]
        if split_input[0].lower() == "get":
            # If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.
            item = current_room.get_item(item_name)
            if item:
                item.on_take()
                # remove the item from the room
                current_room.remove_item(item)
                # Add it to the player's items
                player1.items.append(item)
            else:
                print(f"{item_name} does not exist in room")
        elif split_input[0].lower() == "drop":
            # drop the item
            # check if item is on player
            # if it is:
            #   call item.on_drop()
            #   remove from player
            #   add to room
            pass
        else:
            print("I didn't recognize that command")
            continue
#
#
#