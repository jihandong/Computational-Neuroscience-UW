from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt



# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

tstop = 200
abs_ref = 5 # absolute refractory period 
V_th = 10 # spike threshold

# I: Input current, nA
# noise: amplitude of added noise
def simulation(I, noise=0, label='', color='r'):
    V = 0
    ref = 0 # absolute refractory period counter
    V_trace = []  # voltage trace for plotting
    spiketimes = [] # list of spike times

    # input current
    I += noise*np.random.normal(0, 1, (tstop,)) # nA; Gaussian noise

    for t in range(tstop):
    
       if not ref:
           V = V - (V/(R*C)) + (I[t]/C)
       else:
           ref -= 1
           V = 0.2 * V_th # reset voltage
    
       if V > V_th:
           V = 50 # emit spike
           ref = abs_ref # set refractory counter

       V_trace += [V]

    plt.plot(V_trace, label=label, color=color)

simulation(1, 0, label='noise 0', color='b') 
simulation(1, 1, label='noise 1', color='g') 
simulation(1, 2, label='noise 2', color='y') 
simulation(1, 3, label='noise 3', color='orange') 
simulation(1, 4, label='noise 4', color='red') 
plt.show()
