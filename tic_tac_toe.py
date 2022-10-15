from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coord, get_smart_ai_coord
from menu import get_menu_option


#COLORS
NO_COLOR = "\033[0m" 
RED = "\033[0;31m"
GREEN = "\033[0;32m"
RED_BOX = "\033[7;31m"
GREEN_BOX = "\033[7;32m"
YELLOW = "\033[0;33m"


#GAME MODES
HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_SMART_AI = 4
HUMAN_VS_UNBEATABLE_AI = 5


def play_again():
    '''
    Allows to play again or exit a game.

    Parameters:
        game_type (str): user's choice
        GREEN_BOX (ANSI): green background for a text
        RED_BOX (ANSI): red background for a text
        NO_COLOR (ANSI): clear any color format
    '''
    print(f'\nDo you want to play again? [{GREEN_BOX} Yes {NO_COLOR} / {RED_BOX} No {NO_COLOR}]')
    while True:
        game_type = input('\nWhat is your choice?: ')
        if game_type.upper() == 'YES' or game_type.upper() == 'Y':
            main()
        if game_type.upper() == "NO" or game_type.upper() == 'N':
            print('\nThanks for playing!\nSee you next time!')
            exit()
        print('That\'s not an option. Try again.')


def provide_winner_or_tie(rows, sign):
    '''
    Decides if one of players is a winner or a game ends with a tie.

    Parameters:
        rows (list): board list
        sign (str): currently playing user, an 'X' or an 'O'
        GREEN (ANSI): green color for text
        RED (ANSI): red color for text
        YELLOW (ANSI): red color for text
        NO_COLOR (ANSI): clear any color format
    '''
    print('\n')
    display_board(rows)
    if get_winning_player(rows) == sign:
        if sign == 'X':
            print(f'\n{GREEN}The winner is {sign}!{NO_COLOR}')
        else:
            print(f'\n{RED}The winner is {sign}!{NO_COLOR}')
        play_again()
    if is_board_full(rows):
        print(f'\n{YELLOW}It\'s a tie!{NO_COLOR}')
        play_again()


def main():
    '''
    Game logic.

    Parameters:
        game_mode (int): asks user for preferable game mode and returns options from 1 to 5
        rows (list): board list
        player_1 (str): first player, always an 'X'
        player_2 (str): second player, always an 'O'
        players (list): list of players
        player (str): one of two players
        HUMAN_VS_HUMAN (int): first game mode where two users play with each other, always equal to 1
        RANDOM_AI_VS_RANDOM_AI (int): second game mode where two AIs play with each other, always equal to 2
        HUMAN_VS_RANDOM_AI (int): third game mode where user plays with random AI, always equal to 3
        HUMAN_VS_SMART_AI (int): fourth game mode where user plays with smart AI, always equal to 4
        HUMAN_VS_UNBEATABLE_AI (int): fifth game mode user plays with unbeatable AI, always equal to 5
    '''
    game_mode = get_menu_option()
    rows = get_empty_board()
    print('\n')
    display_board(rows)
    while game_mode != "QUIT":
        player_1 = 'X'
        player_2 = 'O'
        players = [player_1, player_2] 
        if game_mode == HUMAN_VS_HUMAN:
            for player in players:
                if get_winning_player(rows) != player:
                    rows = get_human_coordinates(player, rows)
                    provide_winner_or_tie(rows, player)

        if game_mode == RANDOM_AI_VS_RANDOM_AI:
            for player in players:
                if get_winning_player(rows) != player:
                    rows = get_random_ai_coord(player, rows)
                    provide_winner_or_tie(rows, player)

        if game_mode == HUMAN_VS_RANDOM_AI:
            if get_winning_player(rows) != player_1:
                rows = get_human_coordinates(player_1, rows)
                provide_winner_or_tie(rows, player_1)
            if get_winning_player(rows) != player_2:
                print('\nAI\'s move:')
                rows = get_random_ai_coord(player_2, rows)
                provide_winner_or_tie(rows, player_2)

        if game_mode == HUMAN_VS_SMART_AI:
            if get_winning_player(rows) != player_1:
                rows = get_human_coordinates(player_1, rows)
                provide_winner_or_tie(rows, player_1)
            if get_winning_player(rows) != player_2:
                print('\nAI\'s move:')
                rows = get_smart_ai_coord(player_2, rows)
                provide_winner_or_tie(rows, player_2)


if __name__ == "__main__":
    print('\nWelcome to Tic Tac Toe!')
    main()