import math
import random

odds = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,25,30,31,40,47,61,100,180,500]
bets = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def getOdds():
    pos = random.randint(0, len(odds)-1)
    return str(odds[pos])

def getBet():
    pos = random.randint(0, len(bets)-1)
    return str(bets[pos])

def runQuestion():

    bet = getBet()
    odds = getOdds()
    correctAns = int(bet) * int(odds)
    print("What is $" + bet + " at " + odds + "-1 odds?")
    ans = int(input("Type answer: "))
    if ans == correctAns:
        print("Correct!")
        runQuestion()
    else:
        print("Incorrect... Answer was " + str(correctAns))
        runQuestion()

runQuestion()