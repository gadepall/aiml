<<<<<<< HEAD
=======
#code to plot given set of linear equations


>>>>>>> f531642 (Created codes and figs folder)
from numpy import *
import math
import matplotlib.pyplot as plt


x = linspace(0,5,100)
y1 = (15-3*x)/5
y2 = (10-5*x)/2
plt.plot(x,y1,'r')
plt.plot(x,y2,'g')
plt.ylim(0,10)
plt.xlim(0,10)
plt.fill_between(x,y1,where=y1>0,facecolor='red',alpha=0.5)
plt.fill_between(x,y1,y2,where=y1<y2,facecolor='white',alpha=1)
plt.fill_between(x,y1,y2,where=y2<y1,facecolor='white',alpha=1)
#plt.show()
<<<<<<< HEAD
plt.savefig('/root/ravi/FWC-1/Optimization/optim.png')
=======
#plt.savefig('/root/ravi/FWC-1/Optimization/optim.png')
>>>>>>> f531642 (Created codes and figs folder)
