#Gradient Descent

import numpy as np
import matplotlib.pyplot as plt
import os
import math

import sys       #for path to external scripts
sys.path.insert(0,'/sdcard/Download/parv/CoordGeo')

#local imports
from line.funcs import *
from conics.funcs import *
from triangle.funcs import *
from params import *
#if using termux
import subprocess
import shlex

#Input parameters of the parabola
V = np.array([[1,0],[0,0]])
u = np.array(([0,-2]))
f = 0
R = np.array([[0,1],[-1,0]]) # Rotation matrix

#Input parameters and other points for constrained gradient descent
iters =10000 
alpha = 0.0001
h = np.array(([4,-2]))
eps = 1e-6
n = np.array(([1,-1]))
i = 0
dot_p = 1 


#Generating parabola
num_points = 100
x = np.linspace(-6,6,num_points)
y = 0.25*(x**2)   # y = 0.5*(3-x^2) 
x_old = 4 

#Iterate until the dot product is zero or the iterations are reached
while(i<iters and dot_p != 0):
    y_old = 0.25*(x_old**2) # Parabola point for a given x_old
    q = np.array(([x_old,y_old]))
    m = R@(V@q+u) # Directional vector of tangent at point "q"
    dot_p = m.T@(q-h)
    delta = alpha*x_old
    i=i+1
    x_old = x_old - delta
    #Standard round() is not giving right output. Hence this workaround was used
    dec, integ = np.modf(dot_p)
    dot_p = np.abs(integ+np.round(dec,3))
# Generating normal  
M = line_gen(h,q)
print("The point which minimizes the distance is : ", q)
n = m.T@R
# Generating tangent  
d = (n.T@q)#Intercept for Tangent
tangent_A = np.array([x_old+3,(n[0]*(x_old+3) -d)/(-n[1])])
tangent_B = np.array([x_old-3,(n[0]*(x_old-3) -d)/(-n[1])])
tangent_AB = line_gen(tangent_A, tangent_B)

#Plotting all shapes
plt.plot(x, y,label ='$Parabola$')
plt.plot(M[0],M[1], label='Normal')
plt.plot(tangent_AB[0,:],tangent_AB[1,:] ,label = 'Tangent')

plt.scatter(h[0],h[1])
plt.scatter(q[0], q[1])
#Labeling the coordinates
label = "{}({:.0f},{:.0f})".format('h', h[0],h[1]) #Form label as A(x,y)
plt.annotate(label, # this is the text
            (h[0], h[1]), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(20,0), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best', fontsize = 'small')
plt.grid() # minor
plt.axis('equal')
plt.title('Normal to Parabola Using Gradient Descent')
#if using termux
plt.savefig('/sdcard/Download/latexfiles/optimization/figs/12_6_6_4_gradient.png')
plt.show()
