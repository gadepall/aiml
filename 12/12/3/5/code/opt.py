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


EQ = np.array(( [-1.0, -1.0], [1.0, 0], [-4, 1.0], [1.0, 0], [0,1.0] ))
EQ_b = np.array([-200.0,20.0,0,0,0])
# ax+by+cz >= d
# objective function coeffs
c = np.array([1000.0, 600.0])
x = cp.Variable(2,integer=True)

#Cost function
f = c@x
obj = cp.Maximize(f)
#Constraints
constraints = [EQ@x >= EQ_b]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value:", f.value)
print("optimal var:", x.value.T)

#program to generate graph

x = linspace(0,100,200)
y1=200-x
y2=4*x
plt.plot(x,y1,'b')
plt.plot(x,y2,'g')
plt.ylim(0,200)
plt.xlim(20,100)
plt.fill_between(x,y1,y2,where=y2<y1,facecolor='yellow')
plt.plot(20,180,'o',color='r')
plt.text(20,180,'A(20,180)')
plt.plot(20,80,'o',color='b')
plt.text(20,80,'C(20,80)')
plt.plot(40,160,'o',color='b')
plt.text(40,160,'B(40,160)')
plt.show()
