import numpy as np
from cvxpy import *

#Parabola parameters
P = np.array([2,1]).reshape(2,-1)
V = np.array([[1,0],[0,0]])
u = np.array([0,-1]).reshape(2,-1)

x = Variable((2,1))

#Cost function
f =  quad_form(x-P, np.eye(2))
obj = Minimize(f)

#Constraints
constraints = [quad_form(x,V) + 2*u.T@x <= 0]

#solution
prob = Problem(obj, constraints)
prob.solve()

print(x.value)
