import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
import os
import math

import subprocess 
import shlex
#parabola parameters
V = np.array([[1,0],[0,0]])
u = np.array([0,-2]).reshape(2,1)
f = 0
P = np.array(([4,-2])).reshape(2,1)
# parameters of Tr(AX) expression
A = np.block([[V,u],[u.T,f]])
X = cp.Variable((3,3), symmetric=True)
#parameters of Tr(CX) expression
C = np.block([[np.eye(2),-P],[-P.T, np.linalg.norm(P)**2]])
#defining objective and constraints
objective = cp.Minimize(cp.trace(C @ X))
constraints = [X >> 0]
constraints += [cp.trace(A @ X) == 0,X[2,2] == 1]
# solving the expresssion 
prob = cp.Problem(objective, constraints)
prob.solve()
min_dist = np.sqrt(np.abs(prob.value))
x =X.value
x =np.sqrt(x.diagonal())
print("The point of normal is : ",x)