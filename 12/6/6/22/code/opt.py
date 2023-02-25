import matplotlib.pyplot as plt 
import numpy as np 
from cvxpy import * 

import subprocess 
import shlex
#parabola parameters
V = np.array([[1,0],[0,0]])
u = np.array([0,1]).reshape(2,1)
f = -3
P = np.array(([2, 2])).reshape(2,1)
# parameters of Tr(AX) expression
A = np.block([[V,u],[u.T,f]])
X = Variable((3,3), symmetric=True)
#parameters of Tr(CX) expression
C = np.block([[np.eye(2),-P],[-P.T, np.linalg.norm(P)**2]])
#defining objective and constraints
objective = Minimize(trace(C @ X))
constraints = [X >> 0]
constraints += [trace(A @ X) == 0,X[2,2] == 1]
# solving the expresssion 
prob = Problem(objective, constraints)
prob.solve()
min_dist = np.sqrt(np.abs(prob.value))
x =X.value
x =np.sqrt(x.diagonal())
print(min_dist,x)
plt.savefig('/sdcard/dowload/codes/optimization_assignment/opt.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/download/codes/optimization_assignment/opt.pdf' "))


