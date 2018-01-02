import random as rd
import numpy as np

from ball import Ball
from pool import Pool

### TEST SECTION ###
poolSize = 49

#prepare random
#rd.seed(28469)
print("One random number")
rdEl = rd.randrange(0,49,1,int)
print(rdEl)

print("An array with some random balls")
rdBalls = np.random.randint(1,poolSize+1,poolSize)
#print(balls)

#Generating the pool of the desired size
balls = np.arange(49)
balls = [ el+1 for el in balls]

print("Test of the pool")
poolTest = Pool()
poolTest.fill(balls)
print(poolTest.balls)

popBall = poolTest.pop(48)
print(poolTest.balls)
