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


Z = [1,1]
P = np.array([[1,-1],[1,1],[0,-1],[-1,0]])
Q = np.array([-1,0,0,0])
X = cp.Variable(2,integer = True)
constraints = [P@X <= Q]
objective = cp.Maximize(Z@X)
prob = cp.Problem(objective,constraints)
prob.solve()
if(X.value == None):
    print("There is no feasible region")
    print("No maximum value for Z")
#Calculated points
A = np.array(([0,0]))
B = np.array(([3.5,4.5]))
C = np.array(([-1,0]))
D = np.array(([4,4]))
X1 = np.array(([-1.5,0]))
X2 = np.array(([5,0]))
Y1 = np.array(([0,0]))
Y2 = np.array(([0,5]))
x_AD = line_gen(A,D)
x_CB = line_gen(C,B)
X_Axis= line_gen(X1,X2)
Y_Axis= line_gen(Y1,Y2)


#Plotting all lines
plt.plot(x_AD[0,:],x_AD[1,:],'-r', label='$x-y=-1$')

plt.plot(x_CB[0,:],x_CB[1,:],'-r', label='$-x+y=0$')
plt.plot(X_Axis[0,:],X_Axis[1,:],'-k')
plt.plot(Y_Axis[0,:],Y_Axis[1,:],'-k')

pts1 = [[0.0, 0.0], [4, 0.0], [4, 4]]
pts = np.array(pts1)
hull = ConvexHull(pts)
plt.fill(pts[hull.vertices,0], pts[hull.vertices,1],'red',alpha=0.3,label= '$-x+y<0$')

pts2 = [[-1.0, 0.0], [-1, 4.5], [3.5, 4.5]]
pts = np.array(pts2)
hull = ConvexHull(pts)
plt.fill(pts[hull.vertices,0], pts[hull.vertices,1],'blue',alpha=0.3,label = '$x-y<-1$')
#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D']
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
plt.savefig('/sdcard/sravani21vunnava/trunk/opt_line/fig.pdf')
