# -*- coding: utf-8 -*-

class Ball:
    'Class of one ball of the lottery'
    ballCount = 0
    
    minBallValue = 0
    maxBallValue = 49

    def __init__(self):
        self.nb = 0
        Ball.increaseBallNumber()

    def __init__(self, number):
        if(number < Ball.minBallValue or number > Ball.maxBallValue):
            print("The number assigned to the ball is out of bounds ({1}-{2}) : {0}".format(number,Ball.minBallValue,Ball.maxBallValue))
        self.nb = number
        Ball.increaseBallNumber()

    def displayBallNumber(self):
        strOut = "Total ball number = {0}"
        print(strOut.format(Ball.ballCount))

    def displayBall(self):
        strOut = "ball #{0}"
        print(strOut.format(self.nb))

    def __repr__(self):
        return "ball#{0}".format(self.nb)

    def increaseBallNumber():
        Ball.ballCount+=1
