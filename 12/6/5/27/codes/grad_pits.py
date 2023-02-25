import numpy as np
import matplotlib.pyplot as plt
import os

#Generating points on a circle
def circ_gen(O,r):
	len = 1000
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generate parabola points
def parab_gen(X,a):
    return X**2/a

#Input parameters and other points
X = np.linspace(-4,4,10000)
Y = parab_gen(X,2)
plt.plot(X,Y)
iters = 1000
alpha = 0.01
#Three starting points
s_1 = np.array([[2],[2]])
s_2 = np.array([[-4],[8]])
P = np.array([[0],[5]])
eps = 1e-6
#Function to plot the circle
def plot_circ(p):
    C = circ_gen(P.T,np.linalg.norm(P-p))
    plt.plot(C[0],C[1])

x_old = s_1
i = 0
while(i<iters):
    m = np.array([[1],[x_old[0][0]]])
    delta = alpha*m*(m.T@(P-x_old))
    #Every 50 iterations, we plot the results
    if i%50 == 0:
        plot_circ(x_old)
    i=i+1
    x_old = x_old + delta

M = line_gen(P,x_old)
plt.plot(M[0],M[1])
plt.plot(x_old[0],x_old[1],'k.')
plt.text(x_old[0],x_old[1]+1e-2,'Q')

x_old = s_2
i = 0
while(i<iters):
    m = np.array([[1],[x_old[0][0]]])
    delta = alpha*m*(m.T@(P-x_old))
    #Every 50 iterations, we plot the results
    if i%50 == 0:
        plot_circ(x_old)
    i=i+1
    x_old = x_old + delta

M = line_gen(P,x_old)
plt.plot(M[0],M[1])
plt.plot(x_old[0],x_old[1],'k.')
plt.text(x_old[0],x_old[1]+1e-2,'Q')
plt.plot(P[0],P[1],'k.')
plt.text(P[0]-1e-2,P[1]+1e-2,'P')
plt.grid()
plt.tight_layout()
ax = plt.gca()
ax.set_aspect('equal','box')
plt.savefig('../figs/grad_pits.png')
os.system('termux-open ../figs/grad_pits.png')
