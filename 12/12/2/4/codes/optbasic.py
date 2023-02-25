#Code by Meer Tabres Ali (works on termux)
#To find the Maximum profit by using Optimization
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sympy as sym
from scipy.spatial import ConvexHull
from pylab import *
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
def dir_vec(A,B):
   return B-A
def norm_vec(A,B):
   return np.matmul(omat, dir_vec(A,B))
#if using termux
import subprocess
import shlex
#end if
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
#input parameters
x = cp.Variable(shape=(2,1), name="x")
P = np.array(([1,3]))
Q = np.array(([3,1]))
R = np.array(([12,12]))
V = np.array(([1,3],[3,1]))
z = np.array([17.5,7])

constraints = [cp.matmul(P, x) <= 12, cp.matmul(Q, x) <= 12]
objective = cp.Maximize(cp.matmul(z, x))
problem = cp.Problem(objective, constraints)
solution = problem.solve()


print("------------------------")
print("The Maximum profit is : ");
print("{}".format(round(solution,2)))
print("------------------------")

print("The Maximum Profit is found at")
S=np.linalg.solve(V, R)
#print(x.value)
print(S)
print("------------------------")

#Plotting all lines with calculated points

#Calculated points
O = np.array(([0,0]))
A = np.array(([0,4]))
D = np.array(([12,0]))
B = np.array(([4,0]))
E = np.array(([0,12]))
C = np.array(([3,3]))

x_AD = line_gen(A,D)
x_BE = line_gen(B,E)
x_CA = line_gen(C,A)
x_CB = line_gen(C,B)
x_OD = line_gen(O,D)
x_OE = line_gen(O,E)


#Plotting all lines
plt.plot(x_AD[0,:],x_AD[1,:],'-r', label='$Machine A:x+3y=12$')
plt.plot(x_BE[0,:],x_BE[1,:],'-g', label='$Machine B:3x+y=12$')
plt.plot(x_OD[0,:],x_OD[1,:],'-k')
plt.plot(x_OE[0,:],x_OE[1,:],'-k')

#Labeling the coordinates
tri_coords = np.vstack((A,B,C,O,D,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A(0,4)','B(4,0)','C(3,3)','O(0,0)','D(12,0)','E(0,12)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,3), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('Optimization_basic')

pts1 = [[0.0, 0.0], [0.0, 4.0], [4.0, 0.0], [3.0, 3.0]]
pts = np.array(pts1)
hull = ConvexHull(pts)
plt.fill(pts[hull.vertices,0], pts[hull.vertices,1],'red',alpha=0.3)

#if using termux
plt.savefig('/home/administrator/Assignment7/optfig.pdf')  
plt.show()




