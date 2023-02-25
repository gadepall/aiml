#Gradient Descent

lamda_n = -5 # Start value at lamda_n= -5
#alpha = 0.001 # step size multiplier
alpha = 5.9/8 # step size multiplier
precision = 0.0000001
previous_step_size = 1 
max_count = 10000000 # maximum number of iterations
count = 0 # counter

def func_derivative(x):
    return 8/3*x - 16  # f'(x)

while (previous_step_size > precision) & (count < max_count):
    lamda_n_minus1 = lamda_n
    lamda_n -= alpha * func_derivative(lamda_n_minus1)
    previous_step_size = abs(lamda_n - lamda_n_minus1)
    count+=1

print("The minimum value of function is at", lamda_n)

# Plotting the function 
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/sat/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from params import *
#if using termux
import subprocess
import shlex
#end if

def f(x) :
    return ( 4/3*x**2 -16*x + 64 ) #Objective function


#Plotting 4/3*x**2 -16*x + 64  in Figure 1
x = np.linspace(4,8,100)#points on the x axis
y=  f(x) #Objective function
plt.figure(1)
plt.plot(x,y, label = '$f(\lambda)= 4/3\lambda^2 -16\lambda + 64$')
plt.plot([lamda_n],[f(lamda_n)],marker='o',label='$\lambda_{Min}$')
plt.axis('equal')
plt.grid()
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Minimum Value of Function')
plt.legend(loc = 'best')
plt.savefig('../figs/problem3.1a.pdf')

#plotting lines in Figure 2
O = np.array([0,0])
P = np.array([-2, 2*(math.sqrt(3))])
A = np.array([-8,0])
B = np.array([4, 12/(math.sqrt(3))])

x_OP = line_gen(O,P)
x_AB = line_gen(A,B)

plt.figure(2)

plt.plot(x_OP[0,:],x_OP[1,:],label = "Perpendicular") 
plt.plot(x_AB[0,:],x_AB[1,:] ,label='$x-\sqrt{3}y+8=0$')

plt.scatter(P[0], P[1])
plt.annotate('P', # this is the text
            (P[0], P[1]), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(0,7), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center

plt.legend(loc = 'best')
plt.axis('equal')
plt.grid()
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Perpendicular from Origin')
plt.savefig('../figs/problem3.1b.pdf')

#else
plt.show()
