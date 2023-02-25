import cvxpy as cp
import mpmath as mp
from pylab import*
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/sdcard/Download/10/codes/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#endif
a =cp.Parameter(pos = True)
b =cp.Parameter(pos = True)
x = cp.Variable(pos = True)
y = cp.Variable(pos = True)
A = (a.value+x)*y
objective = cp.Maximize(A)
constraints = []
constraints.append(x<= 2*a)
constraints.append((9*(x**2))+(16*(y**2)) == 144 )
problem = cp.Problem(objective,constraints)
#problem.is_dgp(dpp=True)
a.value=4.0
b.value=3.0#opt= problem.solve()
problem.solve(gp = True)
print("Optimal solution :%d (AREA = %d)" % (problem.value ,   A.value))
'''
plt.figure()
P = np.array(([x1.value,0]))
Q = np.array(([100,0]))
x_PQ = line_gen(P,Q)
plt.plot(x_PQ[0,:],x_PQ[1,:],label ='Feasible region')
'''
'''
tri_coords = np.vstack((P)).T
plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['x=82']
for i ,txt in enumerate(vert_labels):
'''
plt.scatter(P[0],P[1])
plt.scatter(Q[0],Q[1])
plt.annotate('x = 82',(P[0],P[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.annotate('x = 100',(Q[0],Q[1]),textcoords="offset points",xytext=(0,10),ha='center')
plt.xlabel('$X$')
plt.legend(loc = 'best')
#if using termux
plt.savefig('/sdcard/Download/FWC/trunk/optimization/fig.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/FWC/trunk/optimization/fig.pdf'")) 
