
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
import cvxpy  as cp

import sys, os                                          #for path to external scripts

sys.path.insert(0, '/sdcard/Download/10/codes/CoordGeo')        #path to my scripts
#if using termux
import subprocess
import shlex
#end if

#Gradient ascent

#Defining f(x)
def f(x,a,b):
	return (b*(a**2-x**2)**(1/2))+(b/a)*x*(a**2-x**2)**(1/2)
a = 4
b = 3

#For maxima using gradient ascent
cur_x = 1
alpha = 0.001 
precision = 0.0000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: (-2*b*x**2-a*b*x+b*a**2)/(a*(a**2-x**2)**(1/2))           

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

max_val = f(cur_x,a,b)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,a,b)
plt.plot(x,y)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
#if using termux
plt.savefig('/sdcard/Download/FWC/trunk/optimization/fig1.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/FWC/trunk/optimization/fig1.pdf'")) 
#else
#plt.show()

