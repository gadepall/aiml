import numpy as np
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp

#if using termux
import subprocess
import shlex
#end if


A = np.array(( [1, 3], [1, 1]))   
B = np.array([3,2]).reshape(2,1)  

c = np.array([3,5])            
x = cp.Variable((2,1),nonneg=True)

#Cost function
f = c@x     #P = max(1 1)x
obj = cp.Minimize(f)

#Constraints
constraints = [A@x >= B]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("Minimum:", f.value)
print("x", x.value[0])
print("y", x.value[1])
