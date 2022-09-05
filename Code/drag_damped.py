# This file plots the relationship between \theta and time for a damped simple pendulum (with drag force),varying the value of 
# the dimensionless group \epsilon.
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
theta_0 = 5 * math.pi / 180
x0 = 0
dt = 1e-3 * tau
depsilon_vec = [1e-1,1,2]


Lx = 5;# in
Ly = 5;# in
plt.figure(figsize=[Lx, Ly])
ax = plt.axes([0.15, 0.15, 0.8, 0.8], xlim=(0, tf/tau))
plt.xlabel("$t/\\tau$")
plt.ylabel("$\\theta$")
lines = [];
tM=math.floor(tf/dt);
t=np.linspace(0,tf,tM); 

for p in range(len(depsilon_vec)):
    x=np.zeros(tM);
    x[0] = x0;
    theta =np.zeros(tM);
    theta[0] = theta_0;
    epsilon = depsilon_vec[p]
    
    for i in range(tM-1):
        x[i+1] = x[i] - dt * (epsilon*x[i] + (g*math.pow(tau,2)/L)*np.sin(theta[i]))
        theta[i+1] = theta[i] + dt * x[i]

    lines += plt.plot(t/tau,theta*180/math.pi, label="$" + str(epsilon) + "$");
    

labels = [l.get_label() for l in lines]
plt.legend(lines, labels, frameon=True, title="$\\epsilon$")
plt.savefig('drag_damped.png')
plt.show()
