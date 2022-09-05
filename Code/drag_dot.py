# This file plots \theta dot vs \theta for a simple pendulum with drag force. 
from cmath import sin
import math
import numpy as np
import matplotlib.pyplot as plt


g = 9.81; #gravitational constant
L = 1     #rod length 1m
#mu = 1.81 * 1e-5     #air viscosity
#rho = 1.225     #air density
#m = 0.1       #sphere's mass 
#D = 0.01     #1cm = 0.01m
#epsilon = 3*math.pi*mu*D/m        #the dimensionless term 
tau = 2*math.pi*math.sqrt(L/g)
tf = 8 * tau
#theta_0 = 5 * math.pi / 180
x0 = 0
dt = 1e-3 * tau
#depsilon_vec = [1e-2,1e-1,1]
dtheta_vec = [math.pi/18,math.pi/9,math.pi/4]

Lx = 5;# in
Ly = 5;# in
plt.figure(figsize=[Lx, Ly])
ax = plt.axes([0.15, 0.15, 0.8, 0.8])
plt.xlabel("$\\theta$")
plt.ylabel( "$\dot{\\theta}$")
lines = [];
tM=math.floor(tf/dt);
t=np.linspace(0,tf,tM); 

for p in range(len(dtheta_vec)):
    x=np.zeros(tM);
    x[0] = x0;
    theta =np.zeros(tM);
    theta[0] = dtheta_vec[p];
    #epsilon = depsilon_vec[p]
    epsilon = 1
    for i in range(tM-1):
        x[i+1] = x[i] - dt * (epsilon*x[i] + (g*math.pow(tau,2)/L)*np.sin(theta[i]))
        theta[i+1] = theta[i] + dt * x[i]

    lines += plt.plot(theta,x, label="$" + str(round(theta[0]*180/math.pi)) + "$" + "$\\degree$");
    

labels = [l.get_label() for l in lines]
plt.legend(lines, labels, frameon=False, title="$\\theta_{0}$")
plt.savefig('drag_thetaDot.png')
plt.show()
