import numpy as np
import matplotlib.pyplot as plt


#Plotting the circle
#x = 8*np.ones(8)
#y = 6*np.ones(8)
#r = np.arange(8)/np.sqrt(2)
x = 3*np.ones(8)
y = -5*np.ones(8)
r = np.arange(8)*np.sqrt(0.6)/5
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis
# the first axis of these arrays varies the angle, 
# the second varies the circles
x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])

ax=plt.plot(x_line,y_line,'-')

#Plotting the line
x1 = np.linspace(-5,10,100)
x2 = 0.25*(3*x1-26*np.ones(100))

x1_extend = np.linspace(0,20,100)
x2_extend = 0.25*(3*x1-26*np.ones(100))
#)22*np.ones(100) - x1_extend

bx=plt.plot(x1,x2,label="$3x_1-5x_2=26$")

plt.fill_between(x1_extend,x2_extend,color='grey')
plt.fill_between(x1,x2,color='white')
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend( loc='best')

plt.xlim(0, 5)
plt.ylim(-7, -2.5)


plt.savefig('github/optimization/opt/figs/2.4.png')

plt.show()









