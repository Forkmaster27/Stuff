import random
import math as m


def population(size, genrange):
    p = {}
    for i in range(size):
        p[i] = genome(genrange)

    return p

def game_function(epochs, population_size):
    p = population(population_size, 25)
    score = {}
    score_set = 0
    save_file = open("save_file.txt", "w")
    for i in range(epochs):
        for c in range(population_size):
            score[c] = (p[c][0]*p[c][1])/p[c][2]
            if fitness(score[c]) >= score_set:
                score_set = score[c]
                best_player = c
        print(score[best_player])
        save_file.write('Epoch ' + str(i) + ':' + repr(score) + '\n')
        for a in range(population_size):
            p[a] = adjust(p[best_player][0], p[best_player][1], p[best_player][2], miss(score[best_player]))
        print("Fehler: ", miss(score[best_player]))
    var = p[best_player][0],p[best_player][1],p[best_player][2]
    save_file.close()
    return var


def adjust(a, b, c, fehler):
    pm = {}
    for i in range(3):
        pm[i] = random.randint(0,1)
    if pm[0] == 0:
        a -= random.uniform(0.05, fehler)
    elif pm[0] == 1:
        a += random.uniform(0.05, fehler)
    if pm[1] == 0:
        b -= random.uniform(0.05, fehler)
    elif pm[1] == 1:
        b += random.uniform(0.05, fehler)
    if pm[2] == 0:
        c -= random.uniform(0.05, fehler)
    elif pm[2] == 1:
        c += random.uniform(0.05, fehler)

    return (a,b,c)

def miss(output):
    s = 1000
    if output != s:
        f = abs((output - s))
    else:
        f = 0.0000000001
    return f

def fitness(output):
    f = 1/abs((1000-output))
    return f

def genome(range):
    a = random.randint(1, range)
    b = random.randint(1, range)
    c = random.randint(1, range)
    return (a,b,c)

dummy = game_function(50000, 10)
print(dummy)