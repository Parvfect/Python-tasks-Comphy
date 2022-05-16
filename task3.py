import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(-20,20,1.2)
    y = np.arange(-20,20,1.2)
    X,Y = np.meshgrid(x,y)
    xd = X/((X**2 + Y**2)**1.5)
    yd = Y/((X**2 + Y**2)**1.5)
    plt.quiver(X,Y,xd,yd, color = 'r', scale =0.5)
    plt.title("Radiation field Intensity of a Star")
    plt.show()