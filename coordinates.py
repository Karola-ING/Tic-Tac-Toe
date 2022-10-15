import random
from board import get_winning_player, is_board_full


def insert_letter(rows, sign, position):
  '''
  Updates board with new moves.

  PARAMETERS:
    rows (list): board list
    position (str): index of board list
    sign (str): currently playing user, an 'X' or an 'O'

  RETURNS:
    rows (list): new board list
  '''
  rows[int(position)] = sign
  return rows


def get_human_coordinates(sign, rows):
  '''
  Asks user about a place to put an 'X' (or an 'O' if we have two playing users).

  PARAMETERS:
    rows (list): board list
    sign (str): currently playing user, an 'X' or an 'O'
    coordinates (dict): dictionary with parameters user would choose and indexes of board list for them
    user_input (str): user's choice
    key (str): key in dictionary coordinates
    value (int): value in dictionary coordinates

  RETURNS:
    rows (list): new board list
  '''
  coordinates = {'A1': 0, 'A2': 3, 'A3': 6, 'B1': 1, 'B2': 4, 'B3': 7, 'C1': 2, 'C2': 5, 'C3': 8}

  while True:
    user_input = input(f'\nRemember to provide coordinates as e.g. \'A1\' or \'a1\' \n\nPlease, place an {sign} on the board: ')
    if user_input.upper() == 'QUIT':
      print('\nSee you next time!\nThanks for playing!')
      exit()
    if user_input.upper() not in coordinates:
      print('\nYou have to choose proper coordinate. Try again.')
    else:
      for key, value in coordinates.items():
        if user_input.upper() == key:
          if rows[int(value)] == '.':
            rows = insert_letter(rows, sign, value)
            return rows
          else:
            print('\nThat position is taken. Use another one.')
            break
            

def get_random_ai_coord(sign, rows):
  '''
  Choose random place for AI's move.

  PARAMETERS:
    rows (list): board list
    sign (str): currently playing user, an 'X' or an 'O'
    position (list): list of indexes 
    random_position (int): random index 

  RETURNS:
    rows (list): new board list
    or recurrent function if place is occupied
  '''
  if is_board_full(rows):
    return 

  position = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  random_position = random.choice(position)

  if rows[int(random_position)] == '.':
    rows = insert_letter(rows, sign, random_position)
    return rows
  else:
    return get_random_ai_coord(sign, rows)


def smart_ai_best_move(rows):
  '''
  Returns best move for AI.

  PARAMETERS:
    rows (list): board list
    posible_moves (list): all free places on a board
    best_move (int): index of best possible move
    letter (str): element of board list
    move (str): one move from possible_moves
    board_copy (list): copy of rows
    corners_open (list): every free position on a corners of a board
    edges_open (list): every free position on a edges of a board

    RETURNS:
      best_move (int): index of best possible move to make
  '''
  possible_moves = [x for x, letter in enumerate(rows) if letter == '.' and x != 0]
  
  best_move = 0

  for letter in ['O', 'X']:
    for move in possible_moves:
      board_copy = rows[:]
      board_copy[move] = letter
      if get_winning_player(board_copy) == letter:
        best_move = move
        return best_move

  corners_open = []
  for move in possible_moves:
    if move in [0, 2, 6, 8]:
      corners_open.append(move)
  if len(corners_open) > 0:
    best_move = random.choice(corners_open)
    return best_move

  if 4 in possible_moves:
    best_move = 4
    return best_move

  edges_open = []
  for move in possible_moves:
    if move in [1, 3, 5, 7]:
      edges_open.append(move)
  if len(edges_open) > 0:
    best_move = random.choice(edges_open)
    return best_move


def get_smart_ai_coord(sign, rows):
  '''
  Adds AI's move on a board.

  PARAMETERS:
    rows (list): board list
    sign (str): currently playing user, an 'X' or an 'O'
    best_move (int): index of a best move

  RETURNS:
    rows (list): new board list
  '''
  best_move = smart_ai_best_move(rows)
  rows = insert_letter(rows, sign, best_move)
  return rows

