#Python libraries for math and graphics
import numpy as np
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp

#if using termux
import subprocess
import shlex
#end if

# ax+by <= d
A = np.array(( [200, 100], [25, 50]))   #Floor and Fat of cake_1 & cake_2
B = np.array([5000,1000]).reshape(2,1)  #Total available Floor & Fat

# objective function coeffs
c = np.array([1,1])             
x = cp.Variable((2,1),nonneg=True)

#Cost function
f = c@x     #P = max(1 1)x
obj = cp.Maximize(f)

#Constraints
constraints = [A@x <= B]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("Maximun no. of cakes that can me made are:", f.value)
print("Number of type_1 cakes:", x.value[0])
print("Number of type_2 cakes:", x.value[1])
