def get_empty_board():
  '''
  Creates an empty board list.

  PARAMETERS:
    rows (list): board list

  RETURNS:
    rows (list): empty board list
  '''
  rows = ['.' for _ in range(9)]
  return rows

def display_board(rows):
  '''
  Prints board on console.

  PARAMETERS:
    rows (list): board list
    separator (str): separates rows of a board from each other
    board (str): visualisation of a board

  RETURNS:
    print(board) (function): prints visualisation of a board
  '''
  separator = '───┼───┼───'
  board = f'   A   B   C\n1  {rows[0]} | {rows[1]} | {rows[2]}\n  {separator}\n2  {rows[3]} | {rows[4]} | {rows[5]}\n  {separator}\n3  {rows[6]} | {rows[7]} | {rows[8]}'
  return print(board)
  

def is_board_full(rows):
  '''
  Checks if board list has empty spaces.

  PARAMETERS:
    rows (list): board list

  RETURNS:
    True or False
  '''
  if '.' in rows:
    return False
  return True


def get_winning_player(rows):
  '''
  Checks if one of a players win.

  PARAMETERS:
    rows (list): board list

  RETURNS:
    winning players (str): chooses between an 'X' and an 'O'
  '''
  if (rows[6] == 'X' and rows[7] == 'X' and rows[8] == 'X') or (rows[3] == 'X' and rows[4] == 'X' and rows[5] == 'X') or (rows[0] == 'X' and rows[1] == 'X' and rows[2] == 'X') or (rows[0] == 'X' and rows[3] == 'X' and rows[6] == 'X') or (rows[1] == 'X' and rows[4] == 'X' and rows[7] == 'X') or (rows[2] == 'X' and rows[5] == 'X' and rows[8] == 'X') or (rows[0] == 'X' and rows[4] == 'X' and rows[8] == 'X') or (rows[2] == 'X' and rows[4] == 'X' and rows[6] == 'X'):
    return 'X'
  if (rows[6] == 'O' and rows[7] == 'O' and rows[8] == 'O') or (rows[3] == 'O' and rows[4] == 'O' and rows[5] == 'O') or (rows[0] == 'O' and rows[1] == 'O' and rows[2] == 'O') or (rows[0] == 'O' and rows[3] == 'O' and rows[6] == 'O') or (rows[1] == 'O' and rows[4] == 'O' and rows[7] == 'O') or (rows[2] == 'O' and rows[5] == 'O' and rows[8] == 'O') or (rows[0] == 'O' and rows[4] == 'O' and rows[8] == 'O') or (rows[2] == 'O' and rows[4] == 'O' and rows[6] == 'O'):
    return 'O'
