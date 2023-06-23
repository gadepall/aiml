import numpy as np
import pandas as pd
from math import isnan
import matplotlib.pyplot as plt
import os
data = pd.read_excel('marks.xlsx')      #reading input
df1 = data.loc[:,"Total" or "Marks"]    #storing marks column
x = np.array(df1)
x = 100*x/np.max(x)
#Population parameters
mu = df1.mean()
sig = df1.var()
#Get Z-scores
z = (x - mu)/np.sqrt(sig)
N = x.size                              #Size of Data
#x = x.reshape(N,1)                      #Converting to column
#y = np.zeros((N,1))                     #column of Assigned clusters 
#X = np.hstack((x,y))                    #stacking data and cluster
#k = 8                                   #No.of Clusters(Grades)
#
df2 = data.loc[:,"Grade"]
grades = []
s = ""
#Attach grades
for i in range(N):
    if (z[i] >= 3): s = 'A+'
    elif (z[i] >= 2): s = 'A'
    elif (z[i] >= 1): s = 'A-'
    elif (z[i] >= 0): s = 'B'
    elif (z[i] >= -1): s = 'B-'
    elif (z[i] >= -2): s = 'C'
    elif (z[i] >= -3): s = 'D'
    else: s = 'F'
    grades.append(s)

data['Grades'] = grades
data.to_excel('grades_norm.xlsx',index = False)  #writing to file
fig = data['Grades'].value_counts().sort_index(ascending=False).plot.bar().get_figure()
ax = fig.gca()
ax.set_xlabel('Grade')
ax.set_ylabel('Number of Students')
ax.grid()
fig.tight_layout()
fig.savefig('../figs/grades_gauss.png')
os.system('termux-open ../figs/grades_gauss.png')
