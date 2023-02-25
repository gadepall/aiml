import numpy as np
import cvxpy as cp
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
#end if


#input parameters
V = np.array([[1,0],[0,0]])
u = np.array([0,-2]).reshape(2,-1)
h = np.array([4,-2]).reshape(2,-1)
f = 0
R = np.array([[0,1],[-1,0]])


X = cp.Variable((2,1))

#constraints = [((X.T@(V@X))+(2*(u.T@X)))<=0]
constraints = [((cp.quad_form(X,V))+(2*(u.T@X)))<=0]

objective = cp.Minimize(cp.quad_form(X-h, np.eye(2)))

problem = cp.Problem(objective,constraints)

solution = problem.solve()
#print(solution)
print("Point of normal on parabola is : " ,X.value)

#Generating parabola
num_points = 100
x = np.linspace(-10,10,num_points)
y = 0.25*(x**2)   # y = 0.5*(3-x^2)


#generating lines
A = np.array([1.6953,0.7185])
B = np.array([4,-2])
x_AB = line_gen(A,B)


n = np.array(([1,-1.1795])) # Slope of Normal
m = np.array(([1,0.8477])) # Slope of Tangent 

# Generating tangent  
d = n.T@A #Intercept for Tangent
D= np.array(([0,-d]))
tangent_A = 5*m+D  
tangent_B = -5*m+D
tangent_AB = line_gen(tangent_A, tangent_B)
plt.plot(tangent_AB[0,:],tangent_AB[1,:] ,label = 'Tangent')


#Plotting all shapes
plt.plot(x, y,label ='$Parabola$')
plt.plot(x_AB[0,:],x_AB[1,:] ,label = 'normal')


plt.scatter(B[0],B[1])
#Labeling the coordinates
label = "{}({:.0f},{:.0f})".format('P', B[0],B[1]) #Form label as A(x,y)
plt.annotate(label, # this is the text
            (B[0], B[1]), # this is the point to label
            textcoords="offset points", # how to position the text
            xytext=(20,0), # distance from text to points (x,y)
            ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best', fontsize = 'small')
plt.grid() # minor
plt.axis('equal')
plt.title('Normal to Parabola')
#if using termux
#plt.savefig('../figs/problem23.pdf')
plt.title('Normal to parabola')
plt.savefig('/sdcard/Download/latexfiles/optimization/figs/12_6_6_4.png')
plt.show()
