import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import sympy as sym
import math
import sympy
import cvxpy as cp
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB






x = cp.Variable(shape=(2,1), name="x")
A1 = np.array([1,1])
A4=np.array([1,1])
A2 = np.array([1,0])
A3=np.array([0,1])
constraints = [cp.matmul(A1, x) <= 100, cp.matmul(A4, x) >= 60,cp.matmul(A2, x) <= 60 , cp.matmul(A3, x) <= 50]

r = np.array([2.5,1.5])
objective = cp.Minimize(cp.matmul(r, x))

problem = cp.Problem(objective, constraints)
solution = problem.solve()





print("The minimum transportation cost is : ");
print(solution+410)
print("The ration from A to D is : {} ".format((x.value[0])))
print("The ration from A to E is : {} ".format((x.value[1])))
print("The ration from A to F is : {} ".format((100-(x.value[0]+x.value[1]))))
print("The ration from B to D is : {} ".format((60-x.value[0])))
print("The ration from B to E is : {} ".format((50-x.value[1])))
print("The ration from B to F is : {} ".format((x.value[0]+x.value[1]-60)))
