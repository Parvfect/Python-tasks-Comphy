
""" Carnot Cycle 
1. Could add a marker for when isothermal shifts to adibiatic
2. I think its definitely working, but some tests would be nice
"""

import numpy as np
import matplotlib.pyplot as plt

# Gas constant
R = 8.314

def weight_determine(i, h, Nstep):

    if i == 1 or i == Nstep: 
        return h/2.0
    return h

class Isothermal:
    
    def __init__(self, T, minV, maxV):

        self.T = T
        self.minV = minV*10e-3
        self.maxV = maxV*10e-3

    def f(self, v):
        """ Work for isothermal expansion on one mol of gas at a temperature t and volume v """
        return (R * self.T)/v
        

    def trapezoid_integration(self, Nstep):

        delta = (self.maxV - self.minV)/(Nstep-1)
        sumTotal = 0
        x, y = [], []

        for i in range(1, Nstep+1):
            t = self.minV + (i-1)*delta
            w = weight_determine(i, delta, Nstep)
            yt = self.f(t)
            sumTotal += w*yt
            x.append(t)
            y.append(yt)

        return x, y, sumTotal

    def check(self):
        
        resultFormula = R*self.T*np.log(self.maxV/self.minV)
        x,y, resultIntegration = self.trapezoid_integration(1000)
        print("Result using formula = {}, Result using integration = {}".format(resultFormula, resultIntegration))

        plt.plot(x,y)
        plt.title("Work done in Isothermal process = {}".format(resultIntegration))
        plt.xlabel("Volume m^3")
        plt.ylabel("Pressure Pa")
        plt.show()



class Adibiatic:
    
    def __init__(self, T, minV, maxV):

        self.T = T
        self.minV = minV*10e-3
        self.maxV = maxV*10e-3
        self.gamma = 5/3
    

    def f(self, v):
        return ((R*self.T)/v)*(v**self.gamma)
            
    def temperature_change(self, P1, V1, T1, P2, V2):
        return (P2*V2*T1)/(P1*V1)

    def trapezoid_integration(self, Nstep):

        delta = (self.maxV - self.minV)/(Nstep-1)
        sumTotal = 0
        x, y = [], []

        for i in range(1, Nstep+1):
            t = self.minV + (i-1)*delta
            w = weight_determine(i, delta, Nstep)
            yt = self.f(self.minV)/(t**self.gamma)
            sumTotal += w*yt
            x.append(t)
            y.append(yt)

        return x, y, sumTotal

    def check(self):
        
        resultFormula = self.f(self.minV)*(self.maxV**(1-self.gamma)  - self.minV**(1-self.gamma))/(1 - self.gamma)
        x,y, resultIntegration = self.trapezoid_integration(1000)
        print("Result using formula = {}, Result using integration = {}".format(resultFormula, resultIntegration))

        plt.plot(x,y)
        plt.title("Work done in Adibiatic process = {}".format(resultIntegration))
        plt.xlabel("Volume m^3")
        plt.ylabel("Pressure Pa")
        plt.show()
        return resultIntegration


class carnotCycle:
    """ Lordy the temperature changes in an adibiatic change """
    def __init__(self, V0, V1, V2, T):
        self.V0 = V0
        self.V1 = V1
        self.V2 = V2
        self.T = T

    def isoAdiChange(self, T, V0, V1, V2):
        
        X, Y, W = [], [], 0
        x, y, w = [], [], 0
        cycle =  [Isothermal(T, V0, V1), Adibiatic(T, V1, V2)] 
  
        for i in cycle:
            x,y, w = i.trapezoid_integration(1000)
            X.extend(x)
            Y.extend(y)
            W+=w

        T = cycle[1].temperature_change(x[0], y[0], T, x[-1], y[-1])
        
        return X, Y, W, T

    def simulate(self):
        """ Isothermal expansion - Adibatic Expansion - Isothermal Contraction - Adibiatic Contraction """
        X1, Y1, X2, Y2, W = [], [], [], [], 0
        T_h, T_c = 0,0

        # Expansion
        X1, Y1, w, T_c = self.isoAdiChange(self.T, self.V0, self.V1, self.V2)
        W+=w
        
        # Contraction
        X2, Y2, w, T_h = self.isoAdiChange(T_c, self.V2, self.V1, self.V0)
        W+=w

        print("Efficiency is {} %".format((100*(T_h - T_c))/T_h))
        print("Hot temperature is {}".format(T_h))
        print("Cold temperature is {}".format(T_c))
        print(("Work done in Carnot Cycle = {}, which is equal to the heat transferred".format(W)))


        plt.plot(X1, Y1, color = 'red', label = 'Expansion phase')
        plt.plot(X2, Y2, color = 'blue', label = 'Contraction phase')
        plt.title("Efficiency of Carnot Cycle = {:.2f} %".format((100*(T_h - T_c))/T_h))
        plt.xlabel("Volume m^3")
        plt.ylabel("Pressure Pa")
        plt.legend()
        plt.show()
        

def main():
    t = carnotCycle(3000,6000,7000,320)
    t.simulate()