#Gradient Descent

x_n = -5 # Start value at x_n= -5
alpha = 0.001 # step size multiplier
precision = 0.0000001
previous_step_size = 1 
max_count = 10000000 # maximum number of iterations
count = 0 # counter

def func(x):
    return 8*x - 4  # f'(x)

while (previous_step_size > precision) & (count < max_count):
    x_n_minus1 = x_n
    x_n -= alpha * func(x_n_minus1)
    previous_step_size = abs(x_n - x_n_minus1)
    count+=1

print("The minimum value of function is at", x_n)

# Plotting the function 
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

#if using termux
import subprocess
import shlex
#end if

def f(x) :
    return ( (2*x-1)**2 + 3 ) #Objective function

#Plotting (2x-1)**2 +3 
x = np.linspace(-0.5,1.5,40)#points on the x axis
y=  f(x) #Objective function
plt.plot(x,y,color=(0,0,1), label = '$f(x)= (2x-1)^2 + 3$')
plt.plot([x_n],[f(x_n)],color=(1,0,0),marker='o',label="$Min$")
plt.grid()
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Minimum Value of Function')
plt.legend(loc = 'best')
#subprocess.run(shlex.split("termux-open ../figs/1.1.pdf"))
#if using termux
plt.savefig('../figs/Gradient.pdf')
#else
plt.show()
