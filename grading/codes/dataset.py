import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_excel('marks.xlsx')      #reading input
df1 = data.loc[:,"Total" or "Marks"]    #storing marks column
x = np.array(df1)
plt.hist(x)
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/dataset.png')
os.system('termux-open ../figs/dataset.png')
