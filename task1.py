
import math
import matplotlib.pyplot as plt

a = 1

def t1(a):
    f = [math.exp(a*x) for x in range(100)]
    t = range(100)
    plt.plot(t,f)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("f(x) = e^(ax) for a =  {} ".format(a))
    return 

def main():
    t1(a)