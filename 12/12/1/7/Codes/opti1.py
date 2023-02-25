#Python libraries for math and graphics
import numpy as np
#import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/sdcard/Download/Line/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz >= d
A = np.array([[1,1],[1,-2],[1,0],[0,1]])
A_b = np.array([60,0,0,0]).reshape(4,1)
B=np.array([[1,2]])
A_b1=np.array(120).reshape(1,1)
# objective function coeffs
c = np.array([5,10])
x = cp.Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = cp.Minimize(f)
obj1=cp.Maximize(f)
#Constraints
constraint = [ A@x >= A_b,B@x <=A_b1]

#solution
prob = cp.Problem(obj, constraint)
prob.solve()
print("status:", prob.status)
print("min optimal value:", f.value)
print("min optimal var:", x.value.T)
prob = cp.Problem(obj1, constraint)

prob.solve()
print("status:", prob.status)
print("max optimal value:", f.value)
print("max optimal var:", x.value.T)

x=np.linspace(-20,140)
#print(len(x1))
y1=60-x
y2=x/2
y3=(120-x)/2
plt.plot(x,y1,label='x+y=60')
plt.plot(x,y2,label='x-2y=0')
plt.plot(x,y3,label='x+2y=120')
y4=np.zeros(len(x))
plt.plot(x,y4,label='y=0')
plt.plot(y4,x,label='x=0')
plt.title('')
#plt.ylim([-2,8])
# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/sdcard/Download/Opti/figure2/opt1.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/Opti/figure2/opt1.pdf"))
plt.show()
#Footer

