# This file plots the difference between \sin{x} and x to analyze small angle approximation.  
import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,math.pi/2,100)
y_x = x
y_sin = np.sin(x)

plt.figure()
plt.subplot(1,2,1)
plt.xlabel("theta in degrees")
plt.ylabel("Y values")
plt.plot(x*180/math.pi,y_x)
plt.plot(x*180/math.pi,y_sin)
plt.xticks(np.arange(0,90,10))

plt.subplot(1,2,2)
plt.xlabel("theta in degrees")
plt.ylabel("Diff in Y values")
plt.plot(x*180/math.pi,y_x-y_sin)
plt.xticks(np.arange(0,90,10))
plt.yticks(np.arange(0,0.6,0.05))
plt.tight_layout()
plt.savefig("SmallAngle.png")
plt.show()

