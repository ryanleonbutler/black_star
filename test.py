import os
import time
import game_terminal as term
import game_menu as menu
import game_world as world
import game_dialog as dialog
import game_play as actions


if __name__ == '__main__':
    term.clear()

    player_position =  0

    prison_cell = world.Room('Prison Cell', 'Small Window', 'Nothing', 'Nothing', 'Passage', 'Key')
    prison_cell.print_room()
    passage = world.Room('Passage', 'More Passage', 'Nothing', 'Prison Cell', 'Armory', 'Nothing')
    passage.print_room()
    armory = world.Room('Armory', 'Nothing', 'Nothing', 'Passage', 'Nothing', 'Sword')
    armory.print_room()
    prison_cell.right = passage
    passage.left = prison_cell
    passage.down = armory
    armory.left = passage

    world = [prison_cell, passage, armory]
    for i in world:
        print(i.name)

    game = True
    player_position = prison_cell

    while game:

        player_input = term.player_input()

        if player_input.lower() == 'q' or player_input.lower() == 'quit':
            game = False

        elif player_input.lower() == 'h' or player_input.lower() == 'help':
            actions.player_help()

        elif player_input.lower() == 'v' or player_input.lower() == 'view':
            player_position.describe_room()

        elif player_input.lower() == 'u' or player_input.lower() == 'up':
            term.move_to(player_position.up)
            if player_position.up in world:
                player_position = player_position.up
                player_position = player_position.get_room_name()
            else:
                print('Cannot move further. try \'view\' for more options to move to')

        elif player_input.lower() == 'd' or player_input.lower() == 'down':
            term.move_to(player_position.down)
            if player_position.down in world:
                player_position = player_position.down
                player_position = player_position.get_room_name()
            else:
                print('Cannot move further, try \'view\' for more options to move to')

        elif player_input.lower() == 'l' or player_input.lower() == 'left':
            term.move_to(player_position.left)
            if player_position.left in world:
                player_position = player_position.left
                player_position = player_position.get_room_name()
            else:
                print('Cannot move further. try \'view\' for more options to move to')

        elif player_input.lower() == 'r' or player_input.lower() == 'right':
            term.move_to(player_position.right)
            if player_position.right in world:
                player_position = player_position.right
                player_position = player_position.get_room_name()
            else:
                print('Cannot move further. try \'view\' for more options to move to')

        else:
            print('Option does not exist. try \'help\' for more info')