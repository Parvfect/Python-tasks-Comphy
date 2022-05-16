""" Generate Random Numbers and test their distribution """
import matplotlib.pyplot as plt
import numpy as np
import random


class random_check:

    def __init__(self, max_val):
        self.max_val = max_val
    
    def linPlot(self):
        plt.plot(self.i, self.r)
        plt.title("random number ri versus index i")
        plt.xlabel("Position i ")
        plt.ylabel("Random number")
        plt.show()

    def plotPhase(self):
        # Plots ri vs ri+1
        print(self.x)
        plt.plot(self.x, self.y, 'go')
        plt.title("Phase plot of consecutive numbers of a random number sequence")
        plt.xlabel("r_i even random number")
        plt.ylabel("r_{i+1} odd random number")
        plt.show()

    def plotHistogram(self):
        # Plotting histogram 
        plt.title("Histogram of random number vs frequency")
        plt.xlabel("Random number")
        plt.ylabel("Frequency")
        nbin = 40
        plt.hist(self.r, bins=nbin, label="x1")
        plt.show()

    def k_moment(self, k):
        # Testing randomness - calculating kth moment
        self.k = k
        self.kmom = 0
        self.res = 1/(self.k+1)
        for i in range(1, self.max_val+1):
            self.kmom += (1/(self.max_val+1))* (self.r[i-1]**self.k)
        
        self.res2 = (self.kmom - self.res)*np.sqrt(self.max_val)
        return self.kmom, self.res, self.res2
    
    # Nearest neighbour constant
    def nn_check(self, m):
        self.nn = 0
        self.m = m
        for i in range(1, self.max_val + 1 - self.m):
            self.nn += (1/(self.max_val))*self.r[i-1]*self.r[i-1 + self.m]
        return self.nn
        

class LinearCongruentialGenerator(random_check):

    def __init__(self, max_val, a=1140671485, c=128201163, M=2**24, rstart=2030232):
        random_check.__init__(self, max_val)
        self.a = a
        self.c = c
        self.M = M
        self.rstart = rstart

    def generate(self):
        """ Returns random number sequence and ri and ri+1 seqeunces """
        self.r = []
        self.x = []
        self.y = []
        self.i = np.arange(0, self.max_val)

        rcurr = self.rstart
        self.r.append(self.rstart)

        for i in range(1, self.max_val):
            rcurr = (self.a*rcurr + self.c)%self.M
            self.r.append(rcurr)
            

        self.x = [self.r[i] for i in range(len(self.r)) if i%2 == 0]
        self.y = [self.r[i] for i in range(len(self.r)) if i%2 != 0]

        return self.r, self.x, self.y, self.i



class BuiltinRandom(random_check):

    def __init__(self, max_val):
        random_check.__init__(self, max_val)

    def generate(self):
        """ Returns random number seequence using python's inbuilt random.random() function """
        self.r = []
        self.x = []
        self.y = []
        self.i = np.arange(1, self.max_val+1)
        for i in range(1, self.max_val+1):
            self.r.append(random.random())

        self.x = [self.r[i] for i in range(len(self.r)) if i%2 == 0]
        self.y = [self.r[i] for i in range(len(self.r)) if i%2 != 0]

        return self.r, self.x, self.y, self.i   

def main():
    t = LinearCongruentialGenerator(1000)
    t.generate()
    t.plotPhase()
    t.linPlot()
    t.plotHistogram()
    kmom, res2, res3 = t.k_moment(2)
    print("kth moment: ", kmom)
    print("kth moment deviation is: ", res3)
    print("Nearest neighbour constant: ", t.nn_check(2))
