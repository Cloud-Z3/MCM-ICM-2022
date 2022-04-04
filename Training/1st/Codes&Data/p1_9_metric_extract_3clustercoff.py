# Find the cluster coffecient.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
import warnings
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

def getcc(adj,i):
    a=0
    b=0
    for j in range(len(adj)):
        for k in range(len(adj)):
            a+=adj[i][j]*adj[j][k]*adj[i][k]
            b+=adj[i][j]*adj[i][k]
    return a/b if b!=0 else 0

def getccave(adj):
    n=len(adj)
    cc=0
    for i in range(n):
        cc+=getcc(adj,i)
    return cc/n

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
        adj=np.array(adjget(data,player,playerid))
        line[1] = getccave(adj)
        matrix.append(line)
    df = pd.DataFrame(matrix, columns=['TimeSpan', 'Clustering Coefficient'])
    df.to_csv(file2 + '/' + p1 + '/Clustering Coefficient'+str(matchid)+'.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Clustering Coefficient', color='g')
    plt.savefig(file3 + '/p1' + '/Clustering Coefficient'+str(matchid)+'.png')


def considerallmatch():
    passingevents = pd.read_csv(file1 + '/' + 'passingevents.csv')
    matrix=[]
    for i in range(1,39):
        print(i)
        line=[i,0] #MatchID,maxegi
        data = passingevents[passingevents['MatchID'] == i]
        data = data[data['TeamID'] == 'Huskies']
        player, playerid = playerFind(data)
        adj = np.array(adjget(data, player, playerid))
        line[1] = getccave(adj)
        matrix.append(line)
    df=pd.DataFrame(matrix,columns=['MatchID','Clustering Coefficient'])
    df.to_csv(file2+'/'+p1+'/Clustering Coefficient.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='MatchID', y='Clustering Coefficient',color='g')
    plt.savefig(file3 + '/p1' + '/Clustering Coefficient.png')

def considerallmatchaverage():
    matrix=[[i,0] for i in range(1,9)]#TimeSpan, average_max_eigen
    for i in range(1,39):
        df=pd.read_csv(file2 + '/' + p1 + '/Clustering Coefficient'+str(i)+'.csv')
        for j in df.index:
            matrix[j][1]+=df['Clustering Coefficient'][j]
    for i in range(8):
        matrix[i][1]/=39
    df=pd.DataFrame(matrix,columns=['TimeSpan','Clustering Coefficient'])
    df.to_csv(file2 + '/' + p1 + '/Clustering Coefficient_ave.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Clustering Coefficient', color='g')
    plt.savefig(file3 + '/p1' + '/Clustering Coefficient_ave.png')


considerallmatch()

for i in range(1,39):
    print(i)
    considerinmatch(i)

considerallmatchaverage()
