import cvxpy as cp
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import subprocess
import shlex
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
#solution vector
A = np.array(([1,2],[3,1]))
B = np.array([28,24])
x = LA.solve(A,B)
print(x)
print("(i).No of tennis rackets=x=",x[0])
print("No of cricket bats=y=",x[1])


#constraint lines
n1=np.array([1,2])
n2=np.array([3,1])
x=cp.Variable(shape=(2,1),name="x")
co=[cp.matmul(n1,x)<=28,cp.matmul(n2,x)<=24]
Z=np.array([20,10])
obj=cp.Maximize(cp.matmul(Z,x))

P=cp.Problem(obj,co)
sol=P.solve()
print("(ii).Maximum profit=",round(sol,1))

#For plotting
a = np.array([0,14])
b = np.array([14,7])
c= np.array([2,18])
d= np.array([8,0])
x= np.array([4,12])
#generating lines
x_ab = line_gen(a,b)
x_cd = line_gen(c,d)
#Plotting all lines
plt.plot(x_ab[0,:],x_ab[1,:])
plt.plot(x_cd[0,:],x_cd[1,:])
#Labeling the coordinates
tri_coords = np.vstack((x,a,b,c,d)).T
plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['x','a','b','c','d']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis('equal')
#
##if using termux
#plt.savefig('/sdcard/Download/codes/opt_assignment/optm.pdf')
#subprocess.run(shlex.split("termux-open  'storage/emulated/0/Download/codes/opt_assignment/optm.pdf'"))
plt.show()
##test comment

