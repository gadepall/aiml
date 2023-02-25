import numpy as np
import matplotlib.pyplot as plt
import os

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

#Quadratic function
def quad(x):
    return 25*x*x - 34*x + 50
def der(x):
    return 50*x - 34

#Create the quadratic curve
X = np.linspace(17/25-2,17/25+2,1000)
plt.plot(X,quad(X))
alpha = 0.01
lambda_n = -1
eps = 1e-6
cnt = 0
N = 1000000

#Run the gradient descent algorithm
while cnt < N and (abs(alpha*der(lambda_n)) >= eps):
    nxt = lambda_n - alpha*der(lambda_n)
    cnt += 1
    nxt_coord = np.array([[nxt],[quad(nxt)]])
    lambda_coord = np.array([[lambda_n],[quad(lambda_n)]])
    print(nxt)
    L = line_gen(nxt_coord,lambda_coord)
    plt.plot(L[0],L[1],'r')
    plt.plot(lambda_coord[0],lambda_coord[1],'k.')
    plt.plot(nxt_coord[0],nxt_coord[1],'k.')
    lambda_n = nxt

plt.grid()
plt.tight_layout()
plt.savefig('../figs/grad_desc.png')
os.system('termux-open ../figs/grad_desc.png')
