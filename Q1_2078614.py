import csv
import matplotlib.pyplot as plt
import random

def game(ra, rb):
    # Calculating probability of A winning a point
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
print(round(winProbability(70, 30, 100000), 2))

def ability():
    ability = []
    with open('ability.csv') as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr, None)
        for row in rdr:
            ability.append(tuple(int(n) for n in row))
    return ability
print(ability())


def plot():
    graph = [(winProbability(60, 20, 10000), (60/20)), (winProbability(100, 55, 10000), (100/55)), (winProbability(50, 40, 10000), (50/40)), (winProbability(20, 70, 10000), (20/70)), (winProbability(95, 85, 10000), (95/85))]
    x, y = zip(*graph)
    plt.plot(x, y, 'ro')
    plt.ylabel('Ra/Rb')
    plt.xlabel('Probability  "a"  Wins')
    plt.show()
plot()

"""You would first initiallize n to 1 as there has to be a starting game then call the winProbability function. If the
result of the winProbability function is not equal to 0.9 then you want to increment n and call the winProbability function 
again with the new value of n, if it is equal to 0.9 than you just want to print out the value of n and that will be the smallest 
value of n or number of games played so the win probability of 'a' is 0.9. The simulation in the start will always result in the 
winProbability being equal to 1 but as n increases the results of calling the winProbability function will start to become more
accurate."""

# def probabilityaWins(abilityA, abilityB, n):
#     totalProbability = 0.5
#     aWins = 0
#     bWins = 0
#     for _ in range(n):
#         currentMatch = winProbability(abilityA,abilityB,n)
#         if (currentMatch[0] > currentMatch[1]):
#             aWins +=1
#         else:
#             bWins +=1
#     if (max(aWins and bWins)>0):
#         totalProbability = aWins / (aWins + bWins)
#     return totalProbability
# print(probabilityaWins(60,40,5000))