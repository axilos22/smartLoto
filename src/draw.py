from pool import Pool

class Draw:
    """ A draw is a set of ball that has been taken from the pool
        and one number from the luck pool
    """
    maxDraw = 5

    def __init__(self):
        self.balls=[]
        self.luckNb=0

    def addBall(self,ballNb):
        if(len(balls)>= maxDraw):
            print("Maximum size reached. New element has been denied")
            return        
        self.balls.append(ballNb)

    def rmBall(self,ballNb):
        self.balls.remove(ballNb)

    def addLuckNb(self,luckNb):
        self.luckNb=luckNb
