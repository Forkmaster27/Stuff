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
    options.remove((1, 2))  #Fehler
    options.remove((2, 1))
    options.remove((2, 2))

    if len(options) >= 1:
        return options
    else:
        print("BOOO!")

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
    print(board)

def moveleft(board):
    for i in range(4):
        a = []
        for i2 in range(4):
            if board[i][i2] != None:
                a.append(board[i][i2])
                board[i][i2] = None
            else:
                pass

        if len(a) == 1:
            board[i][0] = a[0]


        elif len(a) == 2:

            if a[0] == a[1]:
                board[i][0] = 2 * a[0]

            else:
                board[i][0] = a[0]
                board[i][1] = a[1]


        elif len(a) == 3:

            if a[0] == a[1] != a[2]:
                board[i][0] = 2 * a[0]
                board[i][1] = a[2]

            elif a[0] != a[1] and a[1] == a[2]:
                board[i][0] = a[0]
                board[i][1] = 2 * a[1]

            elif a[0] != a[1] == a[2]:
                board[i][0] = 2 * a[1]
                board[i][1] = a[2]

            elif a[0] != a[1] != a[2]:
                board[i][0] = a[0]
                board[i][1] = a[1]
                board[i][2] = a[2]


        elif len(a) == 4:

            if a[0] == a[1] and a[2] == a[3]:
                board[i][0] = 2 * a[0]
                board[i][1] = 2 * a[2]

            if a[0] == a[1] != a[2] != a[3]:
                board[i][0] = 2 * a[0]
                board[i][1] = a[2]
                board[i][2] = a[3]

            if a[0] != a[1] != a[2] == a[3]:
                board[i][0] = a[0]
                board[i][1] = a[1]
                board[i][2] = 2 * a[2]

            if a[0] != a[1] == a[2] != a[3]:
                board[i][0] = a[0]
                board[i][1] = 2 * a[1]
                board[i][2] = a[3]

            if a[0] != a[1] != a[2] != a[3]:
                pass

    return board

def moveright(board):
    for i in range(4):
        a = []
        for i2 in range(4):
            if board[i][i2] != None:
                a.append(board[i][i2])
                board[i][i2] = None
            else:
                pass

        if len(a) == 1:
            board[i][3] = a[0]


        elif len(a) == 2:

            if a[0] == a[1]:
                board[i][3] = 2 * a[0]

            else:
                board[i][2] = a[0]
                board[i][3] = a[1]


        elif len(a) == 3:

            if a[0] == a[1] != a[2]:
                board[i][2] = 2 * a[0]
                board[i][3] = a[2]

            elif a[0] != a[1] == a[2]:
                board[i][2] = a[0]
                board[i][3] = 2 * a[1]

            elif a[0] == a[1] == a[2]:
                board[i][2] = a[0]
                board[i][3] = 2 * a[1]

            elif a[0] != a[1] != a[2]:
                board[i][1] = a[0]
                board[i][2] = a[1]
                board[i][3] = a[2]




        elif len(a) == 4:

            if a[0] == a[1] and a[2] == a[3]:
                board[i][2] = 2 * a[0]
                board[i][3] = 2 * a[2]

            if a[0] == a[1] != a[2] != a[3]:
                board[i][1] = 2 * a[0]
                board[i][2] = a[2]
                board[i][3] = a[3]

            if a[0] != a[1] != a[2] == a[3]:
                board[i][1] = a[0]
                board[i][2] = a[1]
                board[i][3] = 2 * a[2]

            if a[0] != a[1] == a[2] != a[3]:
                board[i][1] = a[0]
                board[i][2] = 2 * a[1]
                board[i][3] = a[3]

            if a[0] != a[1] != a[2] != a[3]:
                pass

    return board

def moveup(board):
    for i in range(4):
        a = []
        for i2 in range(4):
            if board[i2][i] != None:
                a.append(board[i2][i])
                board[i2][i] = None
            else:
                pass


        if len(a) == 1:
            board[0][i] = a[0]


        elif len(a) == 2:

            if a[0] == a[1]:
                board[0][i] = 2 * a[0]

            else:
                board[0][i] = a[0]
                board[1][i] = a[1]


        elif len(a) == 3:

            if a[0] == a[1] != a[2]:
                board[0][i] = 2 * a[0]
                board[1][i] = a[2]

            elif a[0] != a[1] and a[1] == a[2]:
                board[0][i] = a[0]
                board[1][i] = 2 * a[1]

            elif a[0] != a[1] == a[2]:
                board[0][i] = 2 * a[1]
                board[1][i] = a[2]

            elif a[0] != a[1] != a[2]:
                board[0][i] = a[0]
                board[1][i] = a[1]
                board[2][i] = a[2]


        elif len(a) == 4:

            if a[0] == a[1] and a[2] == a[3]:
                board[0][i] = 2 * a[0]
                board[1][i] = 2 * a[2]

            if a[0] == a[1] != a[2] != a[3]:
                board[0][i] = 2 * a[0]
                board[1][i] = a[2]
                board[2][i] = a[3]

            if a[0] != a[1] != a[2] == a[3]:
                board[0][i] = a[0]
                board[1][i] = a[1]
                board[2][i] = 2 * a[2]

            if a[0] != a[1] == a[2] != a[3]:
                board[0][i] = a[0]
                board[1][i] = 2 * a[1]
                board[2][i] = a[3]

            if a[0] != a[1] != a[2] != a[3]:
                pass

    return board

def movedown(board):        #Fehler
    for i in range(4):
        a = []
        for i2 in range(4):
            if board[i2][i] != None:
                a.append(board[i2][i])
                board[i2][i] = None
            else:
                pass


        if len(a) == 1:
            board[i][3] = a[0]


        elif len(a) == 2:

            if a[0] == a[1]:
                board[i][3] = 2 * a[0]

            else:
                board[i][2] = a[0]
                board[i][3] = a[1]


        elif len(a) == 3:

            if a[0] == a[1] != a[2]:
                board[i][2] = 2 * a[0]
                board[i][3] = a[2]

            elif a[0] != a[1] and a[1] == a[2]:
                board[i][2] = a[0]
                board[i][3] = 2 * a[1]

            elif a[0] != a[1] == a[2]:
                board[i][2] = 2 * a[1]
                board[i][3] = a[2]

            elif a[0] != a[1] != a[2]:
                board[i][1] = a[0]
                board[i][2] = a[1]
                board[i][3] = a[2]


        elif len(a) == 4:

            if a[0] == a[1] and a[2] == a[3]:
                board[i][2] = 2 * a[0]
                board[i][3] = 2 * a[2]

            if a[0] == a[1] != a[2] != a[3]:
                board[i][1] = 2 * a[0]
                board[i][2] = a[2]
                board[i][3] = a[3]

            if a[0] != a[1] != a[2] == a[3]:
                board[i][1] = a[0]
                board[i][2] = a[1]
                board[i][3] = 2 * a[2]

            if a[0] != a[1] == a[2] != a[3]:
                board[i][1] = a[0]
                board[i][2] = 2 * a[1]
                board[i][3] = a[3]

            if a[0] != a[1] != a[2] != a[3]:
                pass

    return board

class game:

    sp = spawn(board)
    actualize(sp[0], sp[1])
    print(board)


    while True:
        x = input("move: ")
        if x == "w":
            board = moveup(board)
            spg = spawn(board)
            actualize(spg[0], spg[1])

        elif x == "a":
            board = moveleft(board)
            spg = spawn(board)
            actualize(spg[0], spg[1])

        elif x == "s":
            board = movedown(board)
            spg = spawn(board)
            actualize(spg[0], spg[1])

        elif x == "d":
            board = moveright(board)
            spg = spawn(board)
            actualize(spg[0], spg[1])

test = game