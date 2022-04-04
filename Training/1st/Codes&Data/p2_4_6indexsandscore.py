from sklearn import tree
import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
import seaborn as sns
import networkx as nx
import matplotlib
import warnings
import copy
warnings.filterwarnings('ignore')
matplotlib.rcParams['font.sans-serif']=['Times New Roman']
#sns.set(style='whitegrid')
file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
file='passingevents_match1.csv'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'

data=pd.read_csv(file2+'/'+p2+'/MatchData.csv')

#columns=['Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient','Shortest-path Length']
columns=['MaxEigenvalue','Connectivity','Clustering Coefficient','Shortest-path Length']

matrix=[]#38场比赛
matrix2=[]
for i in data.index:
    matrix2.append([data['MatchID'][i],data['OwnScore'][i]-data['OpponentScore'][i]])

df2=pd.DataFrame(matrix2,columns=['MatchID','Goal Difference'])
df2['Goal Difference']=(df2['Goal Difference']-min(df2['Goal Difference']))/(max(df2['Goal Difference'])-min(df2['Goal Difference']))
xnew = np.linspace(1, 38, 500)
f = interpolate.interp1d([i for i in range(1,39)], df2['Goal Difference'], kind="quadratic")
ynew = f(xnew)
for i in range(len(xnew)):
    matrix2.append([xnew[i],ynew[i]])
    matrix.append([xnew[i], ynew[i],'Goal Difference'])
for c in columns:
    data[c]=data[c]/max(data[c])
    xnew = np.linspace(1, 38, 500)
    f = interpolate.interp1d(data.index, data[c], kind="quadratic",fill_value="extrapolate")
    ynew = f(xnew)
    for i in range(len(xnew)):
        matrix.append([xnew[i],ynew[i],c])


df=pd.DataFrame(matrix,columns=['MatchID','Value','Index'])
df2=pd.DataFrame(matrix2,columns=['MatchID','Goal Difference'])
plt.figure(dpi=1200, figsize=(12, 8))
sns.lineplot(data=df,x='MatchID',y='Value',hue='Index')
#sns.lineplot(data=df2,x='MatchID',y='Goal Difference')
#plt.show()
plt.savefig(file3 + '/p2' + '/6indexsandscore.png',bbox_inches = 'tight',pad_inches = 0.1)

matrix=[]#8个时间段
for c in columns:
    if c in['Flow Centrality','Team PlayeRank']:
        data = pd.read_csv(file2 + '/' + p2 + '/' + c + '_ave.csv')
    else:
        data=pd.read_csv(file2 + '/' + p1 + '/'+c+'_ave.csv')
    data[c]=data[c]/max(data[c])
    xnew = np.linspace(1, 8, 300)
    f = interpolate.interp1d(data.index, data[c], kind="quadratic",fill_value="extrapolate")
    ynew = f(xnew)
    for i in range(len(xnew)):
        matrix.append([xnew[i],ynew[i],c])
df=pd.DataFrame(matrix,columns=['MatchID','Value','Index'])
plt.figure(dpi=1200, figsize=(14, 8))
sns.lineplot(data=df,x='MatchID',y='Value',hue='Index')
#plt.show()
plt.savefig(file3 + '/p2' + '/6indexsandscore_ave.png',bbox_inches = 'tight',pad_inches = 0.1)
