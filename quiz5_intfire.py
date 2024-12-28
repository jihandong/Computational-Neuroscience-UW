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

def simulation(I, label='', color='r'): # Input current, nA
    V = 0
    ref = 0 # absolute refractory period counter
    V_trace = []  # voltage trace for plotting

    for t in range(tstop):

       if not ref:
           V = V - (V/(R*C)) + (I/C)
       else:
           ref -= 1
           V = 0.2 * V_th # reset voltage

       if V > V_th:
           V = 50 # emit spike
           ref = abs_ref # set refractory counter

       V_trace += [V]

    plt.plot(V_trace, label=label, color=color)

simulation(1000, label='I = 1000nA', color='r')
simulation(0.8, label='I = 0.8nA', color='orange')
simulation(0.4, label='I = 0.4nA', color='yellow')
simulation(0.2, label='I = 0.2nA', color='g')
simulation(0.1, label='I = 0.1nA', color='b')
plt.legend()
plt.show()

# Question16: Since the V0 = 0,
# the threshold current I_th = V_th / R = 0.25 nA = 250 pA
# Quesion17: If I -> +inf,
# The firing period is 1 / 6ms = 133 hz
