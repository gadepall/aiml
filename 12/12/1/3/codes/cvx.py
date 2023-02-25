#code to solve using cvxpy by ravi



import  numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp
x = cp.Variable(shape=(2,1),name="x")
A = np.array([[3,5],[5,2]])
B = np.array([[15],[10]])
constraints = [cp.matmul(A,x)<=B,x>=0,x>=0]
r = np.array([5,3])
objective = cp.Maximize(cp.matmul(r,x))
problem = cp.Problem(objective,constraints)
solution = problem.solve()
print(solution)
print(x.value)

