import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

def f(x,a,b,c,d,e):
    return a*x**4+b*x**3+c*x**2+d*x+e

label_str = "$-x^2 + 2x +9$"

def df(x):
    return 4*a*x**3+3*b*x**2+2*c*x+d

a = 3
b = -8
c = 12
d= -48
e=25
label_str = "$3x^4 - 8x^3 + 12x^2 - 48x + 25$"


#For minima using gradient ascent
cur_x = 0
alpha = 0.001 
precision = 0.000000001 
previous_step_size = 1
max_iters = 100000000 
iters = 100000

#Gradient descent calculation
while (previous_step_size > precision) & (iters <= max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,a,b,c,d,e)

#For maxima 
x1=0
x2=2
x3=3
mn=max(f(x1,a,b,c,d,e),f(x2,a,b,c,d,e),f(x3,a,b,c,d,e))

print("<Minimum value of f(x) is", min_val, "at","x =",cur_x)
print("<Maximum value of f(x) is", mn,"at","x=",x1)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,a,b,c,d,e)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')
plt.plot(x1,mn,'o')
plt.text(0,-11,'Q(0,25)')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()

plt.savefig('/sdcard/opt/opt2.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/opt/opt2.pdf'"))
#plt.show()
