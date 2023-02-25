#Gradient Descent

import numpy as np
import matplotlib.pyplot as plt
import os
import math
from cvxpy import *

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/sat/CoordGeo')
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
u = np.array([0,-2]).reshape(2,-1)
h = np.array([4,-2]).reshape(2,-1)


x = Variable((2,1))

#Cost function
#f =  quad_form(x-h, np.eye(2))
f = norm(x-h)
#f =  power(norm(x-h), 2)
#f =  power(norm_xh, 2)
obj = Minimize(f)

#Constraints
constraints = [quad_form(x,V) + 2*u.T@x <= 0]

#solution
prob = Problem(obj, constraints)
prob.solve()

print(prob.status)

print(f.value,x.value)



