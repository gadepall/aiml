import math
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex

#defining function
def f(x):
	return np.cos(x)**2 + np.sin(x);

#defining derivative of f(x)
df=lambda x: np.cos(x)-2*np.sin(x)*np.cos(x)

#for maxima using gradient ascent
cur_x1=0.5
previous_step_size1=1
iters1=0
precision=0.000000001
alpha=0.0001
max_iters=100000000

while (previous_step_size1>precision)&(iters1<max_iters):
	prev_x=cur_x1
	cur_x1+=alpha*df(prev_x)
	previous_step_size1=abs(cur_x1-prev_x)
	iters1+=1
max_val=f(cur_x1)
print('maximum value of x is',max_val,"at","x=",cur_x1)

#for minima using gradient descent
cur_x2=1.5
previous_step_size2=1
iters2=0

while (previous_step_size2>precision)&(iters2<max_iters):
	prev_x=cur_x2
	cur_x2-=alpha*df(prev_x)
	previous_step_size2=abs(cur_x2-prev_x)
	iters2+=1
    
min_val=f(cur_x2)
print('minimum value of x is',min_val,"at","x=",cur_x2)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x)
label_str = "$cos^2x+sinx$"
plt.plot(x,y,label=label_str)

#Labelling points
plt.plot(cur_x1,max_val,'.',label='point of maxima')
plt.plot(cur_x2,min_val,'.',label='point of minima')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('opt.png')
plt.show()

plt.savefig('/sdcard/Download/fwc-main/Assignment1/opt2.pdf')
