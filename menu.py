def get_menu_option():
    '''
    Allows user to choose type of game or quit a game.

    PARAMETERS:
        game_type (str): user's choice of a game

    RETURNS:
        number (int): game type from 1 to 5
    '''
    print('\nYou can choose your favourite type of a game:\n[1] Human vs Human\n[2] Random AI vs Random AI\n[3] Human vs Random AI\n[4] Human vs Smart AI\n[5] Human vs Unbeatable AI <- in development\nChoose the desired one or type [quit] to leave the game any time.')
    while True:
        game_type = input('\nWhat is your choice?: ')
        if game_type == '1':
            return 1
        if game_type == '2':
            return 2
        if game_type == '3':
            return 3
        if game_type == '4':
            return 4
        if game_type.upper() == "QUIT":
            print('\nThanks for playing!\nSee you next time!')
            exit()
        print('That\'s not an option. Try again.')
