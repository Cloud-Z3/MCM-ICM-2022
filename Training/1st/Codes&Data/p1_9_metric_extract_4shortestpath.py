# Find the Shortest-path Length.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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

def dijkstra(adj,i):
    n=len(adj)
    adjnew=copy.deepcopy(adj)
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
        for j in range(len(uv)):
            if adjnew[i][j]==-1:
                if adjnew[nextdis][j]!=-1:
                    adjnew[i][j]=adjnew[i][nextdis]+adjnew[nextdis][j]
            else:
                if adjnew[nextdis][j]!=-1 and adjnew[i][nextdis]+adjnew[nextdis][j]<adjnew[i][j]:
                    adjnew[i][j]=adjnew[i][nextdis]+adjnew[nextdis][j]
    return sum([item for item in adjnew[i] if item!=-1])

def getshortest(adj):
    n=len(adj)
    ans=0
    for i in range(n):
        ans+=dijkstra(adj,i)
    return ans/n/(n-1)

def adjget(passingevents,player,playerid):
    adjmatrixnew = [[0 for _ in range(len(player))] for _ in range(len(player))]
    for i in passingevents.index:
        a = passingevents['OriginPlayerID'][i].split('_')[1]
        a = playerid[a]
        b = passingevents['DestinationPlayerID'][i].split('_')[1]
        b = playerid[b]
        adjmatrixnew[a][b] += 1
    return adjmatrixnew

def playerFind(passingevents):
    player=list(set(passingevents['OriginPlayerID'])|set(passingevents['DestinationPlayerID']))
    player=[p.split('_')[1] for p in player]
    playerid=dict()
    for i,p in enumerate(player):
        playerid[p]=i
    return player,playerid

def considerinmatch(matchid):
    passingevents=pd.read_csv(file1+'/'+'passingevents.csv')
    passingevents=passingevents[passingevents['TeamID']=='Huskies']
    passingevents=passingevents[passingevents['MatchID']==matchid]
    passingevents['TimeSpan']=[0 for i in range(len(passingevents))]
    for i in passingevents.index:
        passingevents['TimeSpan'][i]=int(passingevents['EventTime'][i]/900)+1
        if passingevents['MatchPeriod'][i]=='2H':
            passingevents['TimeSpan'][i] += 4

    player,playerid=playerFind(passingevents)
    matrix=[]
    for i in range(1,9):
        line=[i,0]
        data=passingevents[passingevents['TimeSpan']==i]
        adj=adjget(data,player,playerid)
        for j in range(len(adj)):
            for k in range(len(adj)):
                if j==k:
                    adj[j][k]=0
                else:
                    if adj[j][k]==0:
                        adj[j][k]=-1
                    else:
                        adj[j][k]=1/adj[j][k]
        line[1] = getshortest(adj)
        matrix.append(line)
    df = pd.DataFrame(matrix, columns=['TimeSpan', 'Shortest-path Length'])
    df.to_csv(file2 + '/' + p1 + '/Shortest-path Length'+str(matchid)+'.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Shortest-path Length', color='g')
    plt.savefig(file3 + '/p1' + '/Shortest-path Length'+str(matchid)+'.png')


def considerallmatch():
    passingevents = pd.read_csv(file1 + '/' + 'passingevents.csv')
    matrix=[]
    for i in range(1,39):
        print(i)
        line=[i,0] #MatchID,maxegi
        data = passingevents[passingevents['MatchID'] == i]
        data = data[data['TeamID'] == 'Huskies']
        player, playerid = playerFind(data)
        adj = adjget(data, player, playerid)
        for j in range(len(adj)):
            for k in range(len(adj)):
                if j == k:
                    adj[j][k] = 0
                else:
                    if adj[j][k] == 0:
                        adj[j][k] = -1
                    else:
                        adj[j][k] = 1 / adj[j][k]
        line[1] = getshortest(adj)
        matrix.append(line)
    df=pd.DataFrame(matrix,columns=['MatchID','Shortest-path Length'])
    df.to_csv(file2+'/'+p1+'/Shortest-path Length.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='MatchID', y='Shortest-path Length',color='g')
    plt.savefig(file3 + '/p1' + '/Shortest-path Length.png')

def considerallmatchaverage():
    matrix=[[i,0] for i in range(1,9)]#TimeSpan, average_max_eigen
    for i in range(1,39):
        df=pd.read_csv(file2 + '/' + p1 + '/Shortest-path Length'+str(i)+'.csv')
        for j in df.index:
            matrix[j][1]+=df['Shortest-path Length'][j]
    for i in range(8):
        matrix[i][1]/=39
    df=pd.DataFrame(matrix,columns=['TimeSpan','Shortest-path Length'])
    df.to_csv(file2 + '/' + p1 + '/Shortest-path Length_ave.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Shortest-path Length', color='g')
    plt.savefig(file3 + '/p1' + '/Shortest-path Length_ave.png')


considerallmatch()

for i in range(1,39):
    print(i)
    considerinmatch(i)

considerallmatchaverage()
