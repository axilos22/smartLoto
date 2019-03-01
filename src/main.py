# GLOBAL import
import importlib
import random as rd
import numpy as np
#LOCAL
from drawing import Drawing

### RULES ###
#Choose 5 numbers between 1 and 49
#Choose 1 number between 1 and 10

numberToPick = 5
minBallNb = 1
maxBallNb = 49
minLuckNb = 1
maxLuckNb = 10

### FUNCTION ###
def generateRandomDraw():
    #Declaring the pool
    pool = np.arange(minBallNb,maxBallNb+1)
    luckNb = np.random.randint(minLuckNb,maxLuckNb+1)
    #Generate random rank
    ranks = np.random.randint(0,maxBallNb+1,numberToPick)
    #Full random draw
    ball1 = pool[ranks[0]]
    ball2 = pool[ranks[1]]
    ball3 = pool[ranks[2]]
    ball4 = pool[ranks[3]]
    ball5 = pool[ranks[4]]
    print("b1={0}\tb2={1}\tb3={2}\tb4={3}\tb5={4}\tL={5}".format(ball1,ball2,ball3,ball4,ball5,luckNb))

testDraw = Drawing("01/01/1990",[1,2,3,4,5],9)
testDraw1 = Drawing("02/01/1990",[5,4,3,2,1],1)
testDraw2 = Drawing("03/01/1990",[1,2,4,3,5],2)
testDraw3 = Drawing("04/01/1990",[49,48,47,46,45],5)

print(testDraw,testDraw1,testDraw2,testDraw3)


