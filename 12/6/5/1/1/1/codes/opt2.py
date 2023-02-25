import numpy as np
import matplotlib.pyplot as plt
import cvxpy  as cp

import sys, os
sys.path.insert(0,'/sdcard/Linearalgebra/CoordGeo')

#if using termux
import subprocess
import shlex
def f(x,a,b,c):
 return a * x**2 + b * x + c 
a = 9
b = 12
c = 2
label_str = "$9x^2 + 12x +2$"

#For minima using gradient descent
cur_x = -1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 2*a*x + b            

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,a,b,c)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,a,b,c)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('/sdcard/Linearalgebra/opt2.pdf')
#plt.show()
