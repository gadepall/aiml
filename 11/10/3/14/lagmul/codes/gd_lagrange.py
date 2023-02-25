import numpy as np
import matplotlib.pyplot as plt
import os

omat = np.array([[0.0, -1.0],[0.0, 1.0]])

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

#intersection of two lines
def line_intersect(n1,c1,n2,c2):
  n=np.vstack((n1.T,n2.T))
  p = np.array([[c1],[c2]])
  #intersection
  p=np.linalg.inv(n)@p
  return p

#Intersection of two lines
def perp_foot(n,cn,P):
  m = omat@n
  cm = (m.T@P)[0][0]
  return line_intersect(n,cn,m,cm)

#Input parameters and other points
iters = 10
alpha = 0.01
x_old = np.array([[0],[-4]])
P = np.array([[-1],[3]])
T = np.array([[16/3],[0]])
eps = 1e-6
n = np.array([[3],[-4]])
m = np.array([[4],[3]])
c = 16
i = 0
L = line_gen(x_old-m,T+m)
plt.plot(L[0],L[1])

#Function to plot the circle
def plot_circ(p):
    C = circ_gen(P.T,np.linalg.norm(P-p))
    plt.plot(C[0],C[1])

while(i<iters):
    delta = alpha*m*(m.T@(P-x_old))
    #Every 2 iterations, we plot the results
    if i%2 == 0: 
        plot_circ(x_old)
    i=i+1
    x_old = x_old + delta

M = line_gen(P,x_old)
plt.plot(M[0],M[1])
plt.plot(P[0],P[1],'k.')
plt.text(P[0]-1e-2,P[1]+1e-2,'P')
plt.plot(x_old[0],x_old[1],'k.')
plt.text(x_old[0],x_old[1]+1e-2,'Q')
plt.grid()
plt.tight_layout()
ax = plt.gca()
ax.set_aspect('equal','box')
plt.savefig('../figs/gd_lagrange.png')
os.system('termux-open ../figs/gd_lagrange.png')
