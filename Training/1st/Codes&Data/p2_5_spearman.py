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
from scipy.stats import spearmanr, pearsonr
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
data['Goal Difference']=data['OwnScore']-data['OpponentScore']
columns=['Goal Difference','Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient','Shortest-path Length']
corr=data[columns]

correlationm=[[0 for _ in range(len(columns))] for _ in range(len(columns))]
for i in range(len(columns)):
    for j in range(len(columns)):
        a=list(data[columns[i]])
        b=list(data[columns[j]])
        correlationm[i][j]=spearmanr(a,b)[0]
print(correlationm)
fig = plt.figure(dpi=1000,figsize=(15,13))
sns.heatmap(correlationm,annot = True,linewidths=1)
#plt.show()
df=pd.DataFrame(correlationm,columns=columns)
df.to_csv(file2 + '/' + p2+'/correlationm_spearman.csv')
plt.savefig(file3 + '/p2' + '/p2_heatmap_spearman.png',bbox_inches = 'tight',pad_inches = 0.1)

correlationm=[[0 for _ in range(len(columns))] for _ in range(len(columns))]
for i in range(len(columns)):
    for j in range(len(columns)):
        a=list(data[columns[i]])
        b=list(data[columns[j]])
        correlationm[i][j]=pearsonr(a,b)[0]
print(correlationm)
fig = plt.figure(dpi=1000,figsize=(15,13))
sns.heatmap(correlationm,annot = True,linewidths=1)
#plt.show()
df=pd.DataFrame(correlationm,columns=columns)
df.to_csv(file2 + '/' + p2+'/correlationm_pearsonr.csv')
plt.savefig(file3 + '/p2' + '/p2_heatmap_pearsonr.png',bbox_inches = 'tight',pad_inches = 0.1)
