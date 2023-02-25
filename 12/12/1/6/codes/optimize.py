
from numpy import *
import math
import  numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp

x = cp.Variable(shape=(2,1),name="x")
A = np.array([[2,1],[1,2]])
B = np.array([[3],[6]])
constraints = [cp.matmul(A,x)<=B,x>=0,x>=0]
r = np.array([1,2])
objective = cp.Maximize(cp.matmul(r,x))
problem = cp.Problem(objective,constraints)
solution = problem.solve()
print(solution)
#print(x.value)

x = linspace(0,10,10)
y = linspace(10,10,10)
y1 = 3-(2*x)
y2 = (6-x)/2
plt.plot(x,y1,'g')
plt.plot(x,y2,'r')
plt.ylim(0,5)
plt.xlim(0,8)
plt.fill_between(x,y,facecolor = 'red',alpha=0.5)
plt.fill_between(x,y1,y2,where=y1<=3,facecolor='white',alpha=1)
plt.fill_between(x,y2,where=y2<=6,facecolor = 'white',alpha=1)
plt.show()
#plt.savefig('/home/shreyani/Downloads/IITH-FWC-main/optimization/figures/optimize.png')
