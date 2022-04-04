from sklearn import tree
import matplotlib.pyplot as plt
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

def dfget(data1,columns,span):
    m1=[]
    for i in span:
        m1.append([data1[c][i] for c in columns])
    X=pd.DataFrame(m1,columns=columns)
    return X

def DTree(span):
    #'Side','CoachID',
    columns=['Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient'\
                ,'Shortest-path Length']
    X=dfget(data,columns,span)
    y=dfget(data,['Outcome'],span)

    clf = tree.DecisionTreeClassifier(random_state=0)
    clf = clf.fit(X, y)
    plt.figure(dpi=2000,figsize=(5,4))
    tree.plot_tree(clf)
    #plt.show()
    plt.savefig(file3+'/'+'p2'+'/Decision Tree.png')

    ans=clf.predict(data[['Flow Centrality','Team PlayeRank','MaxEigenvalue','Connectivity','Clustering Coefficient'\
                ,'Shortest-path Length']])
    return ans

def issame(a,b):
    n=len(a)
    for i in range(n):
        if a[i]!=b[i]:
            return False
    return True

data=pd.read_csv(file2+'/'+p2+'/MatchData.csv')

flag=0
for i in range(1,38):
    for j in range(i+1,38):
        print(i,j)
        span=[k for k in range(38) if k!=i and k!=j]
        a1=list(DTree(span))
        a2=data['Outcome']
        print(list(a1))
        print(list(a2))
        ind=issame(a1,a2)
        print(ind)
        if ind:
            flag=1
            break
    if flag==1:
        break