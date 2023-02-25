import cvxpy as cp
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
omat=np.array(([0,1],[-1,0]))

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
#constraint lines
n1=np.array([1,1])
n2=np.array([5,8])
x=cp.Variable(shape=(2,1),name="x")
co=[cp.matmul(n1,x)<=250,cp.matmul(n2,x)<=1400]
z1=np.array([4500,5000])
obj=cp.Maximize(cp.matmul(z1,x))
p=cp.Problem(obj,co)
sol=p.solve()
print("Maximum profit=",round(sol,1))
#input parameters
x=np.array([0,250])
y=np.array([250,0])
x1=np.array([280,0])
y1=np.array([0,175])
z=np.array([200,50])

#generating the lines
x_xy=line_gen(x,y)
x_x1y1=line_gen(x1,y1)
x_z=LA.solve(x,z)
#plotting all lines
plt.plot(x_xy[0,:],x_xy[1,:],label='$xy$')
plt.plot(x_x1y1[0,:],x_x1y1[1,:],label='$x1y1$')
#Fill under the curve
#plt.fill_between(
  #      x= t, 
   #     y1= t2, 
    #    where= (-1< t)&(t < 0),
     #   color= "k",
      #  alpha= 0.2)

tri_coords = np.vstack((x,y,x1,y1)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['x','y','x1','y1']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#plt.plot('wand.image.shade(gray, azimuth, elevation)')
#plt.title('Parallelogram')
#if using termux
plt.savefig('/home/apiiit-rkv/Desktop/opti.pdf')
#subprocess.run(shlex.split("termux-open '/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-2.pdf'")) 
#else
plt.show()
