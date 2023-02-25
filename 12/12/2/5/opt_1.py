import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import cvxpy as cp

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/bhavani/Documents/CoordGeo')        #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

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
  
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  print(type(N))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

A = np.array(([2,3],[2,1]))
B = np.array([120,80])
#Solution vector
X = LA.solve(A,B)
print(X)
print("(i) . No.of Screws A = x = ",X[0])
print("No.of Screws B = y = ",X[1])

#constraint lines
n1 = np.array([2,3])
n2 = np.array([2,1])
x = cp.Variable(shape=(2,1),name="x")
co = [cp.matmul(n1,x)<=120,cp.matmul(n2,x)<=80]
Z = np.array([7,10])
obj = cp.Maximize(cp.matmul(Z,x))

P = cp.Problem(obj,co)
sol = P.solve()
print("(ii). Maximum profit = ",round(sol,1))

x1 = np.array([60,0])
y1 = np.array([0,40])
x2 = np.array([40,0])
y2 = np.array([0,80])


#generating lines
x_x1y1 = line_gen(x1,y1)
x_x2y2 = line_gen(x2,y2)
#Plotting all lines
plt.plot(x_x1y1[0,:],x_x1y1[1,:])
plt.plot(x_x2y2[0,:],x_x2y2[1,:])

#Labeling the coordinates
tri_coords = np.vstack((X,x1,x2,y1,y2)).T
plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['X','x1','x2','y1','y1']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
##plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
##if using termux
plt.savefig('/home/bhavani/Documents/optimization/opt_linear/op1.pdf')
#subprocess.run(shlex.split("termux-open '/home/bhavani/Documents/optimization/opt_linear/op1.pdf'")) 
##else
plt.show()
##test comment
