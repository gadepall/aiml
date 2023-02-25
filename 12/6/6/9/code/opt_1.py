#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Solving a mensuration problem using cvxpy and geometric programming


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


import sys                                          #for path to external scripts
sys.path.insert(0,'/home/chirag/matrix/CoordGeo')             #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

h=2
Rb=70.0
Rs=45.0

#Declaring Variables
l = cp.Variable(pos=True, name="l")
b = cp.Variable(pos=True, name="b")

#objects
#Total Min cost 
S = Rb*(l*b)+Rs*(2*h*(l+b))

#constraints
constraints = [
        l*b == 4.0
]

#Problem Formulation
problem = cp.Problem(cp.Minimize(S), constraints)

#Checking cuvature of the objective function
print(S.log_log_curvature)

#Checking if the problem is DGP
print("Is this problem DGP?", problem.is_dgp())


#solution
problem.solve(gp=True)
print(problem.value, l.value, b.value)
print("Total min cost is",problem.value)

