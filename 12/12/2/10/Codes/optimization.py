import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if


x = cp.Variable(shape=(2,1), name="x")

A = np.array([[2,1],[3,5]])

B = np.array([[280],[700]])

constraints = [cp.matmul(A, x) <= B, x>=0]

r = np.array([6,5])

objective = cp.Maximize(cp.matmul(r, x))

problem = cp.Problem(objective, constraints)

solution = problem.solve()

print(solution)

print(x.value)

# plotting the constraints lines

x1 = np.linspace(-10,300,100)
y1 = 280 - 2*x1
plt.plot(x1,y1, color="Blue")

x2 = np.linspace(-10,300,100)
y2 = ( 700 - 3*x2) / 5
plt.plot(x2,y2, color="Red")

x3 = [0, 100, 700/3]
y3 = [280, 80, 0]
pts1=['A','B','C']
plt.scatter(x3,y3)


for i, txt in enumerate(pts1):
    plt.annotate(txt, # this is the text
                 (x3[i], y3[i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(2,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#plt.fill_between(x3, y3,color="Cyan",alpha=0.5)
plt.xlabel('$X-axis$')
plt.ylabel('$Y-axis$')
plt.grid() # minor
plt.axis([0,300,0,300])


plt.savefig('/sdcard/Download/optim.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/optim.pdf'"))

plt.show()
