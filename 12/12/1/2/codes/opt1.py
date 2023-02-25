#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/home/user/Documents/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz >= d
A = np.array(([1,2],[3,2]))
A_b = np.array(([8,12])).reshape(2,1)
A1 = np.array(([1,0],[0,1]))
A2 = np.array(([0],[0])).reshape(2,1)
# objective function coeffs
c = np.array(([-3, 4]))
x = cp.Variable([2,1])
#Cost function
f = c@x
obj = cp.Minimize(f)
#Constraints
constraint = [ A@x <= A_b,A1@x >= A2]

#solution
prob = cp.Problem(obj, constraint)
prob.solve()
#print("status:", prob.status)
print("optimal value:", f.value)
print("optimal var:", x.value.T)

x1=np.linspace(0,8,200)
#print(len(x1))
y1=(8-x1)/2
y2=(10-2*x1)/2
plt.plot(x1,y1,label='x+2y=8')
plt.plot(x1,y2,label='3x+2y=12')
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
plt.savefig('/home/user/Documents/Assignments/optimization/fig.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/Download/anusha1/python1/opt1.pdf"))
plt.show()


