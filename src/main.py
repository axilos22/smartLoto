import random as rd
import numpy as np

#from ball import Ball
#from pool import Pool

### RULES ###
#Choose 5 numbers between 1 and 49
#Choose 1 number between 1 and 10

### TEST SECTION ###
numberToPick = 5
minBallNb = 1
maxBallNb = 49

minLuckNb = 1
maxLuckNb = 10

#Declaring the pool
pool = np.arange(minBallNb,maxBallNb+1)
#print(pool)

luckPool = np.arange(minLuckNb,maxLuckNb)
#print(luckPool)

#Generate random rank
ranks = np.random.randint(0,maxBallNb+1,numberToPick)
#print(ranks)

ball1 = pool[ranks[0]]
ball2 = pool[ranks[1]]
ball3 = pool[ranks[2]]
ball4 = pool[ranks[3]]
ball5 = pool[ranks[4]]

print("b1={0}, b2={1}, b3={2}, b4={3}, b5={4},"
    .format(ball1,ball2,ball3,ball4,ball5))


