#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/sdcard/Download/anusha1/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz >= d
A = np.array([[1,2],[2,2],[3,1],[1,0],[0,1]])
A_b = np.array([10,12,8,0,0]).reshape(5,1)
# objective function coeffs
c = np.array([16, 20])
x = cp.Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = cp.Minimize(f)
#Constraints
constraint = [ A@x >= A_b]

#solution
prob = cp.Problem(obj, constraint)
prob.solve()
#print("status:", prob.status)
print("optimal value:", f.value)
print("optimal var:", x.value.T)

x1=np.linspace(0,8,200)
#print(len(x1))
y1=(10-x1)/2
y2=(12-2*x1)/2
y3=(8-3*x1)
plt.plot(x1,y1,label='x+2y=10')
plt.plot(x1,y2,label='2x+2y=12')
plt.plot(x1,y3,label='3x+y=8')
y4=np.zeros(len(x1))
plt.plot(x1,y4,label='y=0')
plt.plot(y4,x1,label='x=0')
plt.title('')
plt.ylim([-2,8])
# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/sdcard/Download/anusha1/python1/opt1.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/anusha1/python1/opt1.pdf"))
plt.show()
