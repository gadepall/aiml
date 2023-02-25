import numpy as np
import matplotlib.pyplot as plt
import os

def f(x): return 25*x*x - 34*x + 50

lam = 17/25
X = np.linspace(lam-2,lam+2,1000)
plt.plot(X,f(X))
plt.plot(lam,f(lam),'k.')
plt.text(lam,f(lam)+5e-1,'$\lambda$')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/convex.png')
os.system('termux-open ../figs/convex.png')
