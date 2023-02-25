import numpy as np
from cvxpy import *

#Parabola parameters
P = np.array([2,1]).reshape(2,-1)
V = np.array([[1,0],[0,0]])
u = np.array([0,-1]).reshape(2,-1)
f = 0
X = Variable((3,3), PSD=True)
C = np.block([[np.eye(2),P],[P.T,np.linalg.norm(P)**2]])
A = np.block([[V,u],[u.T,f]])

#Cost function
cost =  trace(C@X)
obj = Minimize(cost)

#Constraints
constraints = [trace(A@X) <= 0]

#solution
prob = Problem(obj, constraints)
prob.solve()
print(X.value)
