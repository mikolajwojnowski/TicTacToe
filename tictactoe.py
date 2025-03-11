"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state(): #if board is empty, X goes first 
        return X
    
    #if board is not empty, count the number of X and O on the board
    #if X is more than O, then O goes next
    #if O is more than X, then X goes next
    x_count = 0
    o_count = 0
    #count the number of X and O on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    else:
        return X
    
    
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set() #set that contains all possible actions 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: #if the cell is empty we can make a action towards it thus we add it to the set
                actions.add((i, j))
    return actions 


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid action")
    
    new_board = copy.deepcopy(board) #we are creating a new board so that we dont change the original board using deepcopy 
    i, j = action
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
  
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True
    
    # Check if there are any empty cells left
    for row in board:
        if EMPTY in row:
            return False
    
    # If no empty cells and no winner, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    
    return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf #-infinity
    best_action = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = math.inf#infinity
    best_action = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    return v, best_action