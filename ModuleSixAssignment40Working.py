# Room dictionary with moves
rooms = {
    'Living Room': {'South': 'Entry Way', 'East': 'Bedroom', 'West': 'Basement', 'North': 'Upstairs Office',
                    'item': 'None'},
    'Entry Way': {'North': 'Living Room', 'East': 'Garage', 'item': 'Shoes'},
    'Garage': {'West': 'Entry Way', 'item': 'Car'},
    'Basement': {'East': 'Living Room', 'item': 'Safe'},
    'Bathroom': {'South': 'Bedroom', 'item': 'Crazy Ex'},
    'Bedroom': {'North': 'Bathroom', 'West': 'Living Room', 'item': 'Clothing'},
    'Upstairs Office': {'South': 'Living Room', 'East': 'Upstairs Bedroom', 'item': 'Laptop'},
    'Upstairs Bedroom': {'West': 'Upstairs Office', 'item': 'Luggage'},
}

player_inventory = []
winning_inventory = ['Shoes', 'Car', 'Safe', 'Clothing', 'Laptop', 'Luggage']
sorted_winning_inventory = sorted(winning_inventory)
present_location = 'Living Room'

# Introduction and instructions
print('My Crazy Ex!!!!')
print('You just had a major fight with your significant other who is now your crazy ex.\n'
      'Before you can confront your ex to tell them it is over you need to gather your\n'
      'personal belongings to escape, or you might be trapped FOREVER!!!\n')
print('To escape you will need to collect all six items before confronting or ex.\n'
      'Best of luck and godspeed!!!!\n')
print('Move commands: go South, go North, go East, '
      'go West, Type ‘Exit’ to quit game.\n')
print('To collect an item type the name of the item.\n'
      'For example: If the item is a Book.\n'
      'Type "Book"\n')
print('-' * 40)

# Present location function
def show_status(present_location):
    print('You\'re currently in the', present_location)
    print('You currently have', player_inventory, 'in your inventory.')


# Function to move from room to room and return present location
def moves(present_location, player_move):
    for room in rooms:
        if room == present_location:
            if player_move in rooms[present_location]:
                present_location = rooms[present_location][player_move]
                print('-' * 40)

    # Ends game if villain is found
    if present_location == 'Bathroom':
        print('You ran into your crazy ex and you don\'t have all your belongings.')
        print('You are trapped!! Game Over!!')
        quit()

    return present_location

# Function to move item from dictionary and place in inventory
def collect_items(player_move, present_location):
    if 'Crazy Ex' not in player_inventory:
        item = player_move[0].title()
        player_inventory.append(item)
        rooms[present_location]['item'] = 'None'
        winning_inventory.sort()
        player_inventory.sort()
        print('-' * 40)
        print()

        # Player wins if all required items are collected and ends game
        if winning_inventory == player_inventory:
            print('Congratulations!!! You are now free from your Crazy Ex!!')
            print('Thank you for playing!')
            quit()

    else:
        print('Not a valid option!! Try again.\n')

    return player_inventory


def main():
    # Loop for moving between rooms.
    present_location = 'Living Room'

    while present_location != 'Exit':
        show_status(present_location)  # Call function for present location

        # Input player move
        player_move = input('What is your command?\n').split()

        # If player chooses to exit the game call game_over function
        if len(player_move) == 1 and player_move[0].title() == 'Exit':
            print()
            print('-' * 40)
            print('Thank you for playing!!!\nHave a wonderful day.\n')
            present_location = 'Exit'

        # Checks parameters of players input for validity and moves rooms accordingly
        elif len(player_move) == 1 and player_move[0].title() in rooms[present_location]:
            present_location = moves(present_location, player_move[-1].title())
            print()
            print('Item in room {}'.format(rooms[present_location]['item']))

        # Checks parameters of players input for validity and moves rooms accordingly
        elif (len(player_move) == 2 and (player_move[0].lower() == 'go')) \
                and player_move[1].title() in rooms[present_location]:
            present_location = moves(present_location, player_move[-1].title())
            print()
            print('Item in room {}'.format(rooms[present_location]['item']))

        # Checks parameters of players input for validity and calls collect_items function
        elif player_move[0].title() in winning_inventory and player_move[0].title() not in player_inventory:
            if len(player_move) == 1 and player_move[0].title() != 'None' and player_move[0].title() \
                    in rooms[present_location]['item']:
                collect_items(player_move, present_location)

            else:
                print('Not a valid option!! Try again.\n')
                print('-' * 40)
                print('Item in room {}'.format(rooms[present_location]['item']))

        # If move is invalid calls invalid function
        else:
            print('Not a valid option!! Try again.\n')
            print('-' * 40)
            print('Item in room {}'.format(rooms[present_location]['item']))


main()
