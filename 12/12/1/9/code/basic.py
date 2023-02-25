
###########   program to calculate maximum for objective function    ########

import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex



Z= [-1,2]
P= np.array([[1,1],[1,2],[1,0],[0,1]])
Q= np.array([5,6,3,0])

# defining the variable
s= cp.Variable(2, integer=True)

# assigning constraints
constraints = [P@s>=Q] 

# defining ojective
objective= cp.Maximize(Z@s)

#defining the problem
prob= cp.Problem(objective,constraints)


# solving the problem
prob.solve()

#printing the optimum value 
print("status:", prob.status)
print("x and y are :", prob.value)
print("x and y are :", s.value)


#########         program to generate graph      ##########
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

#Generating and plotting line x+y =5
A=np.array([0,5])
B=np.array([5,0])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='x+y=5')

#Generating and plotting line x+2y = 6
C=np.array([0,3])
D=np.array([6,0])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x+2y=6')

#Generating and plotting line x=3
E=np.array([3,0])
F=np.array([3,6])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='x=3')



#Generating and plotting line y=0
G=np.array([-3,0])
H=np.array([8,0])
GH=line_gen(G,H)
plt.plot(GH[0,:],GH[1,:],label='x')

#Generating and plotting line y=0
I=np.array([0,-2])
J=np.array([0,8])
IJ=line_gen(I,J)
plt.plot(IJ[0,:],IJ[1,:],label='y')


#Generating and plotting line -x+2y=1
K=np.array([-1,0])
L=np.array([5,3])
KL=line_gen(K,L)
plt.plot(KL[0,:],KL[1,:],'k--',label='-x+2y=1')


#Shading Required Region
x1=[3,3,4,6]
y1=[4,2,1,0]
plt.fill(x1,y1,alpha=0.5)

x2=[-1,5,5,-2]
y2=[0,3,5,2]
plt.fill(x2,y2,alpha=0.5)

#Labelling points
plt.plot(4,1,'o',color='r')
plt.text(4.2,1.2,'A(4,1)')
plt.plot(6,0 ,'o',color='r')
plt.text(6.5,0.5,'B(6,0)')
plt.plot(3,2,'o',color='r')
plt.text(3.3,2.3,'C(3,2)')
plt.plot(0,0,'o',color='r')
plt.text(0.-0.2,0.-0.2,'O(0,0)')




plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


#plt.savefig('/sdcard/FWCmodule1/optimization/output.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/FWCmodule1/optimization/output.pdf"))
#plt.show()





