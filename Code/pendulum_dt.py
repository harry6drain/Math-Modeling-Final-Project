# This file plots the relationship between \theta and time under different \delta t values for a simple pendulum (no drag).
from cmath import sin
import math
import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['text.usetex'] = True
#plt.rcParams.update({'font.size': 14})

g = 9.81;
L = 1
tau = 2*math.pi*math.sqrt(L/g)
theta_0 = 5 * math.pi / 180
tf = 8 * math.pi * math.sqrt(L/g)
dt_vec = [0.001*tau,0.003*tau,0.005*tau];
u0 = 0
m = 2 #mass of spherical bob
#r = ?

Lx = 5;# in
Ly = 5;# in
plt.figure(figsize=[Lx, Ly])
ax = plt.axes([0.15, 0.15, 0.8, 0.8], xlim=(0, tf/tau))
plt.xlabel("$t/\\tau$")
plt.ylabel("$\\frac{\\theta}{\\theta_{0}}$")
lines = [];

for p in range(len(dt_vec)):
    dt=dt_vec[p];
    tM=math.floor(tf/dt);
    t=np.linspace(0,tf,tM);         #time vector
    u=np.zeros(tM);
    u[0] = u0;      #first time
    theta =np.zeros(tM);
    theta[0] = theta_0;
    for i in range(tM-1):
        u[i+1] = u[i] - dt * (g/L) * math.sin(theta[i]);       
        theta[i+1] = theta[i] + dt * u[i];

    lines += plt.plot(t/tau,theta/theta_0, label="$" + str(round(dt/tau,3)) + "$" + "$\\tau$");
    #print(t[-1])


labels = [l.get_label() for l in lines]
plt.legend(lines, labels, frameon=False, title="$\Delta t\;(\mathrm{s})$")
plt.savefig('pendulum_dt.png')
plt.show()
