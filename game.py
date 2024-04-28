def create_board(n):
    board = []
    for i in range(n):
        board.append(' ')
    return board
    
def place_piece(board, p):
    if p == '▲':
        if '▲' not in board:
            board[0] = '▲'
            return True
        elif board.count('▲') > 0:
            if board[0] == ' ':
                board[0] = '▲'
                return True
            else:
                return False
        else:
            return False
    elif p == '■':
        if '■' not in board:
            board[-1] = '■'
            return True
        elif board.count('■') > 0:
            if board[-1] == ' ':
                board[-1] = '■'
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_move(board, starting_square, ending_square):
  piece = board[starting_square]
  direction = 1 if ending_square > starting_square else -1
  if 0 <= ending_square < len(board):
      if board[ending_square] == ' ':
          if (piece == '▲' and direction == 1) or (piece == '■' and direction == -1):
              return True
  return False

def move_piece(board, starting_square, ending_square):

    piece = board[starting_square]
    if check_move(board, starting_square, ending_square):
        board[ending_square] = piece
        board[starting_square] = ' '

        direction = 1 if ending_square > starting_square else -1

        squares_to_check = range(starting_square + direction, ending_square, direction)

        for square in squares_to_check:
            if board[square] != ' ':
                board[square] = ' '
                break


def moves(board, player):
    for i in range(len(board)):
        if (player == '▲' and board[i] == '▲') or (player == '■' and board[i] == '■'):
            for j in range(len(board)):
                if check_move(board, i, j):
                    return {(i, j)}
    return set()



def choose_move(board, player):
  possible_moves = moves(board, player)
  if possible_moves:
      return possible_moves.pop()
  else:
      return None

