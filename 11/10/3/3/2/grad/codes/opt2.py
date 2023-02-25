import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

#if using termux
import subprocess
import shlex
#end if

#gradient descent to calculate the minimizer
a = 0.001 #step size
T = 1000000 #iterations
lambda1 = 4 #initial value
for i in range(0,T):
    g = 2*lambda1 + 4
    x_1 = lambda1 - a*g
    lambda1 = x_1
print(f"The minimizer is {round(lambda1)}")
lamda_n = round(lambda1)

def f(x) :
    return ( (x**2) +(4*x) + 8 ) #Objective function


#Plottingi x**2 +4*x + 8 
x = np.linspace(-5,1,100)#points on the x axis
y=  f(x) #Objective function
plt.plot(x,y, label = '$f(\lambda)=\lambda^2 +4\lambda + 8$')
plt.plot([lamda_n],[f(lamda_n)],marker='o',label='$\lambda_{Min}=-2$')


plt.axis('equal')
plt.grid()
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Minimum Value of Function')
plt.legend(loc = 'best')
#subprocess.run(shlex.split("termux-open ../figs/1.1.pdf"))
#if using termux
plt.savefig('/sdcard/Download/latexfiles/optimization/figs/opt2.png')
#else
plt.show()
