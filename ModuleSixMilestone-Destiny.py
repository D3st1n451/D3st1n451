# Module 6 Assignment - Destiny Torres

rooms = {
    'Great Hall': {
        'name': 'Great Hall', 'south': 'Bedroom',
    },
    'Bedroom': {
        'name': 'Bedroom', 'east': 'Cellar', 'north': 'Great Hall',
    },
    'Cellar': {
        'name': 'Cellar', 'west': 'Bedroom',
    },
    'Exit': {
        'name': 'Exit',
    }
}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['Great Hall']

while True:
    print('You are in the {}.'.format(current_room['name']))

    if current_room['name'] == 'Cellar':
        print('Congratulations! You have reached the cellar and won the game!')
        break

    elif current_room['name'] == 'Exit':
        print('You can type "quit" to quit the game.')
        pass

    command = input('\nWhich direction do you want to go? ')

    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print('You cannot go that direction. Try again.')

    elif command == 'exit':
        current_room = rooms['Exit']

    elif command == 'quit':
        print('You have quit the game. Thanks for playing!')
        break

    else:
        print('Input invalid. Try again.')
