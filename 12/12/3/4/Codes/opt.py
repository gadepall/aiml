import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if

x1 = np.linspace(-10,100,100)
y1 = 60 - 2*x1
plt.plot(x1,y1, color="Blue")

x2 = []
y2 = np.linspace(-10,100,100)
for i in y2:
    x2.append(20)
plt.plot(x2,y2, color="Red")

x3 = np.linspace(-10,100,100)
y3 = ( 120 - 2*x3 ) / 3
plt.plot(x3,y3, color="Green")

x4 = [0, 15, 20, 20]
y4 = [40, 30, 20, 0]
pts1=['A','B','C','D']
plt.scatter(x4,y4)


for i, txt in enumerate(pts1):
    plt.annotate(txt, # this is the text
                 (x4[i], y4[i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(2,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#plt.fill_between(x4, y4,color="Cyan",alpha=0.5)
plt.xlabel('$X-axis$')
plt.ylabel('$Y-axis$')
plt.grid() # minor
plt.axis([0,70,0,70])

x = cp.Variable(shape=(2,1), name="x")
A = np.array([[2,1],[1,0],[2,3]])
B = np.array([[60],[20],[120]])

constraints = [cp.matmul(A, x) <= B, x>=0]
r = np.array([7.5,5])
objective = cp.Maximize(cp.matmul(r, x))

problem = cp.Problem(objective, constraints)

solution = problem.solve()
print(solution)
print(x.value)

#plt.savefig('/sdcard/Download/circlfig.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/Download/circlefig.pdf'"))

plt.show()
