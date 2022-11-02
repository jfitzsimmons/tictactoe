"""
Tic Tac Toe Player
"""

import math
import copy

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
    flatBoard = [item for sublist in board for item in sublist]
    turnsMod2 = (len(flatBoard) - flatBoard.count(EMPTY)) % 2

    if turnsMod2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    _actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                _actions.append((i, j))
    return _actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i < 0 or i > 2 or j < 0 or j > 2 or len(action) != 2:
        raise Exception("impossible action")

    _board = copy.deepcopy(board)
    _board[i][j] = player(_board)
    return _board


def winner(board):
    _board = board

    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        for j in range(3):
            if _board[i][j] != EMPTY:
                if i == 0:
                    # across
                    if _board[i][j] == _board[i+1][j] and _board[i+1][j] == _board[i+2][j]:
                        return _board[i][j]
                    # diagnol top left
                    if j == 0:
                        if _board[i][j] == _board[i+1][j+1] and _board[i+1][j+1] == _board[i+2][j+2]:
                            return _board[i][j]
                    # diagnol bottom left
                    if j == 2:
                        if _board[i][j] == _board[i+1][j-1] and _board[i+1][j-1] == _board[i+2][j-2]:
                            return _board[i][j]
                # vertical
                if j == 0:
                    if _board[i][j] == _board[i][j+1] and _board[i][j+1] == _board[i][j+2]:
                        return _board[i][j]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCount = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                emptyCount += 1

    if emptyCount == 0 or winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    _winner = winner(board)
    if _winner == X:
        return 1
    elif _winner == O:
        return -1
    else:
        return 0


def getMinValue(board):
    if terminal(board) == True:
        return utility(board)
    bestScore = float('inf')
    for action in actions(board):
        bestScore = min(bestScore, getMaxValue(result(board, action)))
    return bestScore


def getMaxValue(board):
    if terminal(board) == True:
        return utility(board)
    bestScore = float('-inf')
    for action in actions(board):
        bestScore = max(bestScore, getMinValue(result(board, action)))
    return bestScore


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    bestMove = (-1, -1)
    _player = player(board)

    if _player == X:
        bestScore = float('-inf')
    else:
        bestScore = float('inf')

    for action in actions(board):
        _result = result(board, action)
        if _player == X:
            newScore = getMinValue(_result)
        else:
            newScore = getMaxValue(_result)

        if (newScore > bestScore and _player == X) or (newScore < bestScore and _player == O):
            bestMove = action
            bestScore = newScore

    return bestMove
