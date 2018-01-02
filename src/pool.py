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
    
    def __init__(self,minSize=minPoolSize,maxSize=maxPoolSize):
        self.balls = []        
        self.size = len(self.balls)
        self.minSize = minSize
        self.maxSize = maxSize
        
    def fill(self,fillTable):
        fillSize = len(fillTable)
        if(fillSize < self.minSize or fillSize > self.maxSize):
            print("Size table out of bounds : {0} not in [{1};{2}]"
                  .format(fillSize,self.minSize,self.maxSize))
            return
        self.balls = fillTable
        
    def pop(self,rank):
        return self.balls.pop(rank-1)
    
        
