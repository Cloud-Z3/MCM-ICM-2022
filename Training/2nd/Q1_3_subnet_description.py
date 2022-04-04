import pandas as pd
import numpy as np
from collections import Counter
import os
# from Q1_lib import *
from copy import deepcopy

def getcc(adj,i):
    print(i)
    a=0
    b=0
    for j in range(len(adj)):
        if adj[i][j]==0 and adj[j][i]==0:
            continue
        for k in range(len(adj)):
            if adj[i][k]==0 and adj[k][i]==0:
                continue
            else:
                b+=1
                if adj[j][k]==1 or adj[k][j]==1:
                    a+=1
            # a+=adj[i][j]*adj[j][k]*adj[i][k]
            # b+=adj[i][j]*adj[i][k]
    return a/b if b!=0 else 0

def getccave(adj):
    n=len(adj)
    cc=0
    for i in range(n):
        cc+=getcc(adj,i)
    return cc/n

def dijkstra(adj,i):
    n=len(adj)
    # print(adj)
    adjnew=adj
    unvisited=set(range(n))
    unvisited.remove(i)
    while True:
        distance=[]
        for j in unvisited:
            if adjnew[i][j]!=-1:
                distance.append([adjnew[i][j],j])
        if len(distance)==0:
            break
        distance.sort()
        nextdis=distance[0][1]
        unvisited.remove(nextdis)
        uv=list(unvisited)
        for j in uv:
            if adjnew[i][j]==-1:
                # print(1)
                if adjnew[nextdis][j]!=-1:
                    # print(3)
                    adjnew[i][j]=adjnew[i][nextdis]+adjnew[nextdis][j]
            else:
                # print(2)
                if adjnew[nextdis][j]!=-1 and adjnew[i][nextdis]+adjnew[nextdis][j]<adjnew[i][j]:
                    adjnew[i][j]=adjnew[i][nextdis]+adjnew[nextdis][j]
    # print(adjnew)
    return sum([item for item in adjnew[i] if item!=-1]),sum([1 for item in adjnew[i] if item!=-1 and item!=0])

def descript(nodefile,edgefile):
    df_node=pd.read_csv(nodefile)
    df_edge=pd.read_csv(edgefile)
    print(len(df_node))
    print(len(df_edge))
    musician=list(df_node['Label'])
    n=len(musician)
    mu_id=dict()
    for i,m in enumerate(musician):
        mu_id[m]=i
    adj=[[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        adj[i][i]=0
    for i in df_edge.index:
        a=df_edge['Source'][i]
        b=df_edge['Target'][i]
        if adj[a][b]==-1:
            adj[a][b]=1
        else:
            adj[a][b]+=1
    # print(adj)

    flow_centrality=sum([sum([j if j!=-1 else 0 for j in adj[i]]) for i in range(n)])*2/n
    print(flow_centrality)

    pathnum=0
    pathsum=0
    for i in range(n//10):
        print(i)
        ps,pn=dijkstra(adj,i)
        pathsum+=ps
        pathnum+=pn
        #print(ps,pn)
    # print(ps,pn)
    average_path_length=pathsum/pathnum if pathnum!=0 else 1
    print(average_path_length)

    adj = [[0 for _ in range(n)] for _ in range(n)]
    for i in df_edge.index:
        a = df_edge['Source'][i]
        b = df_edge['Target'][i]
        adj[a][b] += 1
    cluster_coffecient=getccave(adj)
    print(cluster_coffecient)

    return flow_centrality,average_path_length,cluster_coffecient

if __name__=='__main__':
    for i in range(16):
        # if i==1:
        #     break
        print(i)
        nodefile=f'./Data/p1/subnet_edge&data/nodes_{str(i)}.csv'
        edgefile=f'./Data/p1/subnet_edge&data/edges_{str(i)}.csv'
        for item in zip(['flow_centrality','average_path_length','cluster_coffecient'],descript(nodefile,edgefile)):
            print(item)

