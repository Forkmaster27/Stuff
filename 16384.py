import numpy as np
import random as rd

board = np.array([[None, None, None, None],
                  [None, None, None, None],
                  [None, None, None, None],
                  [None, None, None, None]])


def spawn_options(board):
    options = []
    for i in range(4):
        for i2 in range(4):
            if board[i][i2] == None:
                options.append((i, i2))

    options.remove((1, 1))
    options.remove((1, 2))
    options.remove((2, 1))
    options.remove((2, 2))

    return options


def spawn(board):
    options = spawn_options(board)
    twofour = rd.randint(1,10)
    position = options[rd.randint(0, len(options)-1)]
    if twofour == 10:
        return (position, 4)
    else:
        return (position, 2)


def actualize(pos, value):
    a = pos[0]
    b = pos[1]
    board[a][b] = value

def move():
    move = input()
    if move == "w":
        board[any()]