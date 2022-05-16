"""
Task 6
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


def multiwalk(Nstep, Nwalk, x0=0, y0=0):
    """ Returns average distance for N walks of N steps each """

    x, y, Rtot = 0, 0, 0
    for i in range(1, Nwalk+1):
        x,y = random_walk(Nstep, x0, y0)
        Rtot += random_walk_displacement(x, y)
    
    return Rtot/Nwalk
    
def square_walk(Nstep, a):
    """ Random walk from vertices of a square with side a """

    Rav1 = multiwalk(Nstep, 100, 0, 0)
    Rav2 = multiwalk(Nstep, 100, a, 0)
    Rav3 = multiwalk(Nstep, 100, 0, a)
    Rav4 = multiwalk(Nstep, 100, a, a)
    
    plt.plot([0, 0], [a, 0], 'k-', [a, 0], [a, a], 'k-', [a, a], [0, a], 'k-', [0, a], [0, 0], 'k-')
    circle1 = plt.Circle((0, 0), Rav1, color='r', fill=False)
    circle2 = plt.Circle((a, 0), Rav2, color='b', fill=False)
    circle3 = plt.Circle((0, a), Rav3, color='g', fill=False)
    circle4 = plt.Circle((a, a), Rav4, color='y', fill=False)

        
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(circle3)
    plt.gca().add_patch(circle4)
    plt.plot(0,0, marker='o', color='r')
    plt.plot(a,0, marker='o', color='b')
    plt.plot(0,a, marker='o', color='g')
    plt.plot(a,a, marker='o', color='y')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title("Random Walk from Vertices of a Square - Ravg for square of length {}".format(a))
    plt.show()

def main():
    square_walk(1000, 10)
    