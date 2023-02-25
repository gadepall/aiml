import numpy as np
import cvxpy as cp

#DGP Optimization
# DGP requires Variables to be declared positive via `pos=True`.
r = cp.Variable(pos=True, name = "r")  #Radius of cone
h = cp.Variable(pos=True, name = "h")  #Height of cone

objective_fn = 1/3*cp.power(r,2)*h
constraints = [h <= 1, r<=1, h*h + r*r <= 1]
problem = cp.Problem(cp.Maximize(objective_fn), constraints)
print(objective_fn.log_log_curvature)

#Checking if the problem is DGP
print("Is this problem DGP?", problem.is_dgp())

problem.solve(gp=True)

print("r: ", r.value)
print("h: ", h.value)
print("Semi verical angle: ", np.arctan(r.value/h.value))
