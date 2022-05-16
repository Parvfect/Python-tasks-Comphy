"""
Task 5
"""


import numpy as np
import matplotlib.pyplot as plt
import random



def random_walk(steps, x0=0, y0=0):
    """ Returns vector x and y for random walk of N steps with initial values x0, y0"""

    x, y, xc, yc = [], [], 0, 0
    x.append(x0)
    y.append(y0)

    # Step through loop
    for i in range(steps):

        #For each step choose which direction to go
        xc += (random.random()-0.5)*2
        yc += (random.random()-0.5)*2

        # Add the new position to the list
        x.append(xc)
        y.append(yc)

    return x, y



def random_walk_displacement(x, y):
    """
    Calculate the displacement of the random walk
    """
    return np.sqrt((x[-1]- x[0])**2 + (y[-1]- y[0])**2)


def plot_random_walk(x, y):
    """
    Plot the random walk
    """
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Random Walk {} steps'.format(len(x)))
    plt.arrow(x[0], y[0], x[-1], y[-1], color='r', linewidth=4)
    plt.show()


def multiwalk(Nstep, Nwalk):
    """ Returns average distance for N walks of N steps each """

    x, y, Rtot = 0, 0, 0
    for i in range(1, Nwalk+1):
        x,y = random_walk(Nstep)
        Rtot += random_walk_displacement(x, y)
    
    return Rtot/Nwalk
    
def multiwalk_avg(Nwalk, minNStep, maxNStep, stepInterval):

    steps = []
    displacement = []

    for i in range(minNStep, maxNStep, stepInterval):
        steps.append(i)
        displacement.append(multiwalk(i, Nwalk))    
    
    return steps, displacement

def RvsN():
    
    N, R = multiwalk_avg(100, 100, 10000, 1000)
    plt.plot(N, R)
    plt.xlabel('Number of steps')
    plt.ylabel('Displacement')
    plt.title('Random walk displacement')
    plt.show()
    
def main():
    plot_random_walk(*random_walk(1000))
    RvsN()

    