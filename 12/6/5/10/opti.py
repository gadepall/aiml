import matplotlib.pyplot as plt
import numpy as np

import subprocess
import shlex

def f(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

def df(x):
    return 3*a*x**2+2*b*x+c

a = 2
b = 0
c = -24
d =107
label_str = "$2x^3-24x+107$"


#For maxima using gradient ascent
cur_x = 1
alpha = 0.001
precision = 0.000000001 
previous_step_size = 1
max_iters = 1000000 
iters = 1000

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  
    

max_val = f(cur_x,a,b,c,d)
print("<Maximum value of f(x) is", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-9,10,50)
y=f(x,a,b,c,d)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')
#plt.plot(cur_x1,max_val1,'o')
#plt.text(cur_x1, max_val1,f'P({cur_x1:.4f},{max_val1:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#plt.savefig('/sdcard/FWC/Opt/Opt-2/opt2.png')
plt.show()
