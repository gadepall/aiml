import math
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex

#defining function
def f(x):
	return x**4 - 62*x**2 + 120*x+9;

#defining derivative of f(x)
df=lambda x: 4*x**3-124*x+120

#for maxima using gradient ascent
cur_x1=4
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


#Plotting f(x)
x=np.linspace(0,20,50)
y=f(x)
label_str = "$x^4 - 62x^2 + 120x + 9$"
plt.plot(x,y,label=label_str)

#Labelling points
plt.plot(cur_x1,max_val,'.',label='point of maxima')


plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('opt.png')
plt.show()

#plt.savefig('/sdcard/Linearalgebra/opt2.pdf')

