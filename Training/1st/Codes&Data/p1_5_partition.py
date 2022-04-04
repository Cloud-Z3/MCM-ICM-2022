# This is a demo, or, let's say, a lib.
# It's only for match1, considering 15 min timespan.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
matplotlib.rcParams['font.sans-serif']=['Times New Roman']

file1='2020_Problem_D_DATA'
file2='2020_Problem_D_DATA_After_Pro'
file3='Image'
file='passingevents_match1.csv'
p1='Problem1'
p2='Problem2'
p3='Problem3'
p4='Problem4'

def simplemap(coordinate):
    x1=0
    y1=-50
    span=10
    x=coordinate[0]
    y=coordinate[1]
    return [x1+x*2,y1+y*1]

def nodeedgeget(file):
    passingevents_match1=pd.read_csv(file2+'/'+p1+file)
    num=len(passingevents_match1)

    nodes=[]
    for i in passingevents_match1.index:
        if passingevents_match1['TeamID'][i]=='Huskies':
            nodes.append(passingevents_match1['OriginPlayerID'][i])
            nodes.append(passingevents_match1['DestinationPlayerID'][i])
    nodes=list(set(nodes))#节点

    nodeid=dict()
    for i in range(len(nodes)):
        nodeid[nodes[i]]=i

    adjmatrix=[[0 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for i in range(num):
        if passingevents_match1['TeamID'][i] != 'Huskies':
            continue
        a=passingevents_match1['OriginPlayerID'][i]
        b=passingevents_match1['DestinationPlayerID'][i]
        adjmatrix[nodeid[a]][nodeid[b]]+=1
    return adjmatrix

adjmatrix=nodeedgeget('/passingevents_match1.csv')
#df_nodes.to_csv(file2+'/'+p1+'/'+'dataforp1_1_node.csv',index=False)
#df_edges.to_csv(file2+'/'+p1+'/'+'dataforp1_1_edge.csv',index=False)

def greedyselection2(adjmatrix):
    ans=[]
    for i in range(len(adjmatrix)):
        for j in range(i+1,len(adjmatrix)):
            if adjmatrix[i][j]!=0:
                ans.append([adjmatrix[i][j]+adjmatrix[j][i],[i,j]])
    ans.sort(reverse=True)
    return ans

def greedyselection3(adjmatrix):
    ans=[]
    adjmatrixnew=adjmatrix.copy()
    l=len(adjmatrixnew)
    for i in range(l):
        for j in range(i+1,l):
            adjmatrixnew[i][j]+=adjmatrixnew[j][i]
    for i in range(l):
        for j in range(i+1,l):
            a=adjmatrixnew[i][j]
            for k in range(j+1,l):
                b=adjmatrixnew[i][k]
                c=adjmatrixnew[j][k]
                if a==0 or b==0 or c==0:
                    continue
                ans.append([a+b+c,[i,j,k]])
    ans.sort(reverse=True)
    return ans

ans=greedyselection2(adjmatrix)
for a in ans:
    print(a)
ans=greedyselection3(adjmatrix)
for a in ans:
    print(a)