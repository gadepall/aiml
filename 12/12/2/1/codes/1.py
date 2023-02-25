import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


import sys, os                                          #for path to external scripts
sys.path.insert(0,'\sdcard\Download\chinna\optimization\CoordGeo')

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz = d
EQ = np.array(( [3.0, 4.0], [5.0, 2.0]))
EQ_b = np.array([8.0,11.0]).reshape(2,1)
# ax+by+cz >= d
# objective function coeffs
c = np.array([60.0, 80.0])

x = cp.Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = cp.Minimize(f)
#Constraints
constraints = [EQ@x >= EQ_b]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value:", f.value)
print("optimal var:", x.value.T)

#if using termux
#plt.savefig(os.path.join(script_dir, fig_relative))
#subprocess.run(shlex.split("termux-open "+os.path.join(script_dir, fig_relative)))
#else
#plt.show()
