# -*- coding: utf-8 -*-
import numpy as np

from ball import Ball

class Pool:
    """ The pool is all the existing balls that are pickable.
    All the possible balls will exist into the pool.
    Then during one draw, the balls will be removed from the pool"""
    minPoolSize = 1
    maxPoolSize = 49
    normalPoolsize= 49
    
    def __init__(self):
        self.balls = []        
        self.size = len(self.balls)
        
    def __init__(self,balls):
        self.size = len(balls)
        if(self.size < Pool.minPoolSize or
           self.size > Pool.maxPoolSize):
            print("the Pool size is out of bounds [{1}-{2}] : {0}"
                  .format(self.size,
                          Pool.minPoolSize,
                          Pool.maxPoolSize))
        self.balls = balls
        
        
