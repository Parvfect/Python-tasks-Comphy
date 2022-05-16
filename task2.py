'''
Projectile motion calculator
Parameters:
h: height
v: initial velocity
theta: angle of launch
'''    

import math
import numpy as np
import matplotlib.pyplot as plt

# acceleration due to gravity
g = 9.81

def projectile(h, v, theta):
    
    # Converting angle to radians 
    theta = math.radians(theta)

    # Finding components of velocity
    Vx = v*math.cos(theta)
    Vy = v*math.sin(theta)

    # Finding Time of flight
    T = (Vy + math.sqrt(Vy**2 + 2*g*h))/g
    
    # Finding Range of flight
    l = (Vx* (Vy + math.sqrt(Vy**2 + 2*g*h)))/g
    
    # Finding Maxiumum height reached
    h = (h + Vy**2)/(2*g)

    return T, l, h

def plot_projectile(h, theta, T, v):

    # Creating a discrete time array
    t = np.arange(0, T, 0.01)

    # Finding position of projectile as a function of time
    x = v*t*math.cos(theta)
    y = h + v*t*math.sin(theta) - 0.5*g*t**2

    # Plotting the projectile
    plt.plot(x, y)
    plt.xlabel('x-coordinate') 
    plt.ylabel('y-coordinate')
    plt.title('Projectile Motion - h = {:.2f}m, theta = {:.2f}deg, v = {:.2f}ms'.format(h, theta, v))
    plt.show()

def main():

    print("Projectile motion calculator")
    print("Enter the following parameters:")
    
    h = float(input("Height (m): "))
    v = float(input("Initial velocity (m/s): "))
    theta = float(input("Angle of launch (degrees): "))
    
    T, l, H = projectile(h, v, theta)
    
    print("Time of flight: {:.2f}s".format(T))
    print("Distance travelled: {:.2f}m".format(l))
    print("Maximum Height: {:.2f}m".format(h))
    
    plot_projectile(h, math.radians(theta), T, v)