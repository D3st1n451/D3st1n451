def show_intro():
    # Print intro
    print('Vampire in School!', '\n',
          'STORYLINE', '\n',
          'You are on a special call for your side job as a vampire hunter, you received a call ', '\n',
          'about a vampire sighting in the catholic elementary school. You must defeat the ', '\n',
          'vampire before morning, when the students come; but you will need to find vampire fighting', '\n',
          'tools. You will need pencils from the classroom, garlic cloves from the school garden, mirror ', '\n',
          'from the science lab, hair spray from the girl’s locker room, cross in school ', '\n',
          'church, and a lighter from the teachers lounge. There are two other rooms: the ', '\n',
          'library, principles office, and the gym. The water must be achieved before ', '\n',
          'the cross, without the water the cross cannot be picked up. The vampire is in the ', '\n',
          'basement, if the basement is entered without all the tools, you will be kicked back to start.', '\n',
          'Save the school!', '\n')


def show_instructions():
    print('Vampire In School!')
    print('\n', 'Instructions', '\n',
          'To move about, type commands: go South, go North, go East, go West', '\n',
          'To add an item to your backpack, type: grab item ', '\n',
          'To get the current game status, type: status', '\n',
          'To show the instructions again, type: instructions', '\n',
          'To quit the game, type: quit.', '\n',
          '___________________________________________________________________________')


def move_between_rooms(current_room, move, rooms):
    current_room = rooms[current_room][move]
    return current_room


def grab_item(current_room, rooms, backpack):
    backpack.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of connecting rooms with items
    global move
    rooms = {
        'Parking Lot': {'East': 'Library'},
        'Library': {'North': 'Science Lab', 'South': 'Basement'},
        'Garden': {'East': 'Science Lab', 'item': 'Garlic'},
        'Classroom': {'East': 'Teachers Lounge', 'South': 'Gym', 'West': 'Science Lab',
                      'North': 'Cafeteria', 'item': 'Pencil'},
        'Cafeteria': {'South': 'Classroom', 'item': 'Water'},
        'Gym': {'North': 'Classroom', 'East': 'Girls Locker Room', 'South': 'Church'},
        'Church': {'North': 'Gym', 'East': 'Basement', 'item': 'Cross'},
        'Girls Locker Room': {'West': 'Gym', 'item': 'Hair Spray'},
        'Teachers Lounge': {'West': 'Classroom', 'North': 'Principals Office', 'item': 'Lighter'},
        'Principals Office': {'South': 'Teachers Lounge'},
        'Science Lab': {'South': 'Library', 'North': 'Basement', 'West': 'Garden',
                        'East': 'Classroom', 'item': 'Mirror'},
        'Basement': ''
    }
    # list for storing player backpack
    backpack = []
    # starting room
    current_room = 'Parking Lot'
    # show introduction
    show_intro()
    # show instructions
    show_instructions()

    while True:
        # when player reaches the basement
        if current_room == 'Basement':
            # winning case
            if len(backpack) == 7:
                print('You encountered the Vampire! With all the items you were able to '
                      'defeat him and save the school. Congratulations!')
                print('Thank you for playing Vampire in School.')
                break
            # Backpack with less than 7 items
            else:
                print('Woah there, you are not that strong.', '\n',
                      'You charged into the basement and was defeated by the vampire!', '\n'
                      'Better luck next time! Thanks for playing!')
                break
        # Current room, and backpack items
        print('You are in the ' + current_room)

        if not backpack:
            print('You do not have any items in your backpack.')
        else:
            print('Your backpack contains:', ', '.join(backpack))

        # tell the user if there is an item in the room
        if current_room != 'Basement' and 'item' in rooms[current_room].keys():
            print('You found the {}, let\'s pick it up.'.format(rooms[current_room]['item']), '\n',
                  '_______________________________________________')
        # prompt for a move
        move = input('Enter your next move: '
                     '').title().split()
        print()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You picked up the {}'.format(rooms[current_room]['item']))
            print('___________________________________________________________')
            grab_item(current_room, rooms, backpack)
            continue
        # handle if the user enters a command to show status
        elif move == ['Status']:
            continue
        # handle if the user enters a command to show instructions
        elif move == ['Instructions']:
            show_instructions()
            continue
        # handle if the user enters a command to quit game
        elif move == ['Quit']:
            print('You have quit the game.')
            break
        # handle if the user enters an invalid command
        else:
            print('Invalid command, please try again')
            continue


main()
