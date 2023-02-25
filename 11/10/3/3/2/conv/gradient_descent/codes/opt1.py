import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import subprocess
import shlex
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def line_gen(A,B):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB

#gradient descent to calculate the minimizer
a = 0.001 #step size
T = 1000000 #iterations
lambda1 = 4 #initial value
for i in range(0,T):
    g = 2*lambda1 + 4
    x_1 = lambda1 - a*g
    lambda1 = x_1
print(f"The minimizer is {round(lambda1)}")

#line parameters
O = np.array([0,0])
A = np.array([2,2])
B = np.array([-2,2])
m = np.array([1,0])

#minimizer point calculation
P = A + (round(lambda1)*m)
D = np.linalg.norm(P-O)

print(f"The minimizer point is {P}")
print(f"The distance is {D}")

#line generation
x_AB = line_gen(A,B)
x_OP = line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$[0 1]x-2=0$')
plt.plot(x_OP[0,:],x_OP[1,:],label='$perpendicular$')

tri_coords = np.vstack((O,P)).T
plt.scatter(tri_coords[0,:],tri_coords[1,:])

vert_labels = ['O','P']
for i, txt in enumerate(vert_labels):
    label = "{}({:.0f},{:.0f})".format(txt, tri_coords[0,i],tri_coords[1,i]) #Form label as A(x,y)
    plt.annotate(label, # this is the text
            (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.savefig('/sdcard/Download/latexfiles/optimization/figs/opt1.png')
plt.show()
