import matplotlib.pyplot as plt
import random
import csv
import numpy as np
from scipy.interpolate import make_interp_spline

# Simulating a single game for the PARS scoring system
def game(ra, rb):
    p = ra / (ra + rb)
    a_score = 0
    b_score = 0
    # Looping through the function until one of the players score reaches 11 or have a difference of two points
    while a_score <= 10 and b_score <= 10 or abs(a_score - b_score) <= 2:
        r = random.random()
        if r<p:
            a_score += 1
        else:
            b_score += 1
    return a_score, b_score
random.seed(57)
print(game(70, 30))

# Win probability for n games
def winProbability(ra, rb, n):
    As_win = 0
    Bs_win = 0
    for _ in range(n):
        a_score, b_score = game(ra, rb)
        a_win = a_score > b_score
        if a_win:
            As_win += 1
        else:
            Bs_win += 1
        # print(a_win)
    p = As_win / (As_win + Bs_win)
    return p
print(round(winProbability(70, 30, 10000), 2))

# Generating a tuple list using values in a csv
def ability():
    ability = []
    with open('ValuesforGame.csv') as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr, None)
        for row in rdr:
            ability.append(tuple(int(n) for n in row))
    return ability
print(ability())

# Simulating a game for the English Scoring system
def game2(ra, rb):
    pa_win = ra / (ra + rb)
    a_score = 0
    b_score = 0

    A = 'a'
    B = 'b'
    players = [A, B]
    server = random.choice(players)
    # print(server)

    while a_score < 9 and b_score < 9:
        r = random.random()
        print(r)
        if r <= pa_win and server == A:
            a_score += 1
        elif r <= pa_win and server == B:
            server = A
            # print(server)
        if r > pa_win and server == B:
            b_score += 1
        elif r > pa_win and server == A:
            server = B
            # print(server)
    return a_score, b_score
print(game2(70, 30))

# Calculating the win porbability with English scoring for n games
def winProbability2(ra, rb, n):
    As_win = 0
    Bs_win = 0
    for _ in range(n):
        a_score, b_score = game2(ra, rb)
        a_win = a_score > b_score
        if a_win:
            As_win += 1
        else:
            Bs_win += 1
        # print(a_win)
    pa_wins = As_win / (As_win + Bs_win)
    return pa_wins
print(round(winProbability2(70, 30, 5000), 2))

# Generating a list of tuples using csv values
def ability2():
    ability = []
    with open('ValuesforGame.csv') as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr, None)
        for row in rdr:
            ability.append(tuple(int(n) for n in row))
    return ability
print(ability2())

# Generating a graph for the results
def plot2():
    numgames = 100000
    x1 = np.array([winProbability(60, 20, numgames), winProbability(100, 55, numgames), winProbability(50, 40, numgames), winProbability(20, 70, numgames), winProbability(95, 85, numgames), winProbability(70, 30, numgames), winProbability(60, 50, numgames), winProbability(68, 86, numgames), winProbability(83, 89, numgames), winProbability(63, 59, numgames), winProbability(89, 84, numgames), winProbability(70, 78, numgames)])
    y1 = np.array([(60/20), (100/55), (50/40), (20/70), (95/85), (70/30), (60/50), (68/86), (83/89), (63/59), (89/84), (70/78)])
    points = zip(x1, y1)
    points = sorted(points, key=lambda point: point[0])
    x1, y1 = zip(*points)
    x1_smooth = np.linspace (min(x1), max(x1), 300)
    y1_smooth = make_interp_spline(x1, y1)(x1_smooth)
    plt.plot(y1_smooth, x1_smooth, label = "Point-a-Rally Scoring (PARS)")
    x2 = np.array([winProbability2(60, 20, numgames), winProbability2(100, 55, numgames), winProbability2(50, 40, numgames), winProbability2(20, 70, numgames), winProbability2(95, 85, numgames), winProbability2(70, 30, numgames), winProbability2(60, 50, numgames), winProbability2(68, 86, numgames), winProbability2(83, 89, numgames), winProbability2(63, 59, numgames), winProbability2(89, 84, numgames), winProbability2(70, 78, numgames)])
    y2 = np.array([(60/20), (100/55), (50/40), (20/70), (95/85), (70/30), (60/50), (68/86), (83/89), (63/59), (89/84), (70/78)])
    points2 = zip(x2, y2)
    points2 = sorted(points2, key=lambda point: point[0])
    x2, y2 = zip(*points2)
    x2_smooth = np.linspace (min(x2), max(x2), 300)
    y2_smooth = make_interp_spline(x2, y2)(x2_smooth)
    plt.plot(y2_smooth, x2_smooth, label = "English Scoring")
    plt.xlabel('Ra/Rb')
    plt.ylabel('Probability  "a"  Wins')
    plt.legend()
    plt.show()
plot2()





