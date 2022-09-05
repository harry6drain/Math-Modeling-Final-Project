# This file plots the relationship between \theta and time for a simple pendulum (no drag) under fixed \delta t value, while 
# varying the value for \theta_{0}.
from cmath import sin
import math
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

g = 9.81;
L = 1
tf = 10 * math.pi * math.sqrt(L/g)
tau = 2 * math.pi * math.sqrt(L/g)
dt = 1e-3 * tau
dtheta_vec = [math.pi/36,math.pi/9,math.pi/4]
u0 = 0

Lx = 5;# in
Ly = 5;# in
plt.figure(figsize=[Lx, Ly])
ax = plt.axes([0.15, 0.15, 0.8, 0.8], xlim=(0, tf/tau))
plt.xlabel("$t/\\tau$")
plt.ylabel("$\\theta$")
lines = []
tM=math.floor(tf/dt);
t=np.linspace(0,tf,tM);
nmr_hue=['-r','-g','-b']
anlc_hue = ['--r','--g','--b']

for p in range(len(dtheta_vec)): 
    u=np.zeros(tM);
    theta = np.zeros(tM)
    u[0] = u0
    theta[0] = dtheta_vec[p]
    anlc = theta[0]*np.cos(math.sqrt(g/L)*t)
    for i in range(tM-1):
        theta[i+1] = theta[i] + dt * u[i];
        u[i+1] = u[i] - dt * (g/L) * np.sin(theta[i]);       
        
    lines += plt.plot(t/tau,theta*180/math.pi,nmr_hue[p],label="$" + str(round(theta[0]*180/math.pi)) + "$" + "$\\degree$");
    lines += plt.plot(t/tau,anlc*180/math.pi,anlc_hue[p],label="$" + str(round(theta[0]*180/math.pi)) + "$" + "$\\degree$");
    

    
    
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, frameon=False, title="Initial $\\theta$")
plt.savefig('pendulum_dTheta.png')
plt.show()
