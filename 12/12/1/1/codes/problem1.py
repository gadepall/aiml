#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import cvxpy  as cp

#if using termux
import subprocess
import shlex
#end if


# objective function coeffs
c = np.array(([3, 4]))
x = cp.Variable([2,1])

#Cost function
cost_func = c@x
obj = cp.Maximize(cost_func)

#Constraints
constr = np.array(([1,4],[-1,0],[0,-1]))
constr_b = np.array(([4,0,0])).reshape(3,1)
constraint = [ constr@x <= constr_b]


#solution
prob = cp.Problem(obj, constraint)
prob.solve()
print("optimal value:", cost_func.value)
print("optimal var:", x.value.T)

#Drawing lines
x1 = np.linspace(0,5,400)#points on the x axis
y1 = (4-x1)/4
y2 = np.zeros(len(x1))


plt.plot(x1,y1,label = '$x+4y=4$')
plt.plot(x1,y2,label = '$y=0$')
plt.plot(y2,x1,label = '$x=0$')

plt.grid()
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Linear Programming')
plt.ylim(-0.5,1.5)
#txt = "{} {}".format("Optimum ", "Point") 
#plt.plot(x.value[0],x.value[1],color=(1,0,1),marker='o',label= txt)

#Filling the feasible region
fill_cords = np.array(([0,0],[0,1],x.value.T.ravel()))
txt = "{} {}".format("Feasible ", "Region") 
plt.fill("j", "k", 'plum',label = txt,
         data={"j": fill_cords[:,0],
               "k": fill_cords[:,1]})  
#Corner Points
A = np.array(([0, 1]))
B = np.array(([0, 0]))
x1 = round(x.value[0,0])
x2 = round(x.value[1,0])
x = np.array(([x1, x2]))

#Labeling the coordinates
tri_coords = np.vstack((A,B,x)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','x']
for i, txt in enumerate(vert_labels):
    label = "{}({},{})".format(txt, int(tri_coords[0,i]),int(tri_coords[1,i])) #Form label as A(x,y)
    plt.annotate(label, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.legend(loc='best')
#if using termux
plt.savefig('../figs/problem1.pdf')
#else
plt.show()
