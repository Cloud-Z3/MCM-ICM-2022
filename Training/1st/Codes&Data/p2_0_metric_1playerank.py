# Find the Team PlayeRank.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
import warnings
import copy
import math
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

def TeamPlayeRankget(data):
    n=len(data)
    ans=1
    player, playerid=playerFind(data)
    ave=[0 for _ in range(len(player))]
    for i in data.index:
        ave[playerid[data['OriginPlayerID'][i].split('_')[1]]]+=1
    for i in range(len(ave)):
        ave[i]/=n
    for a in ave:
        ans*=a
    ans=ans**(1/len(player)) if len(player)!=0 else 0
    return ans

def adjget(passingevents,player,playerid):
    adjmatrixnew = [[0 for _ in range(len(player))] for _ in range(len(player))]
    for i in passingevents.index:
        a = passingevents['OriginPlayerID'][i].split('_')[1]
        a = playerid[a]
        #b = passingevents['DestinationPlayerID'][i].split('_')[1]
        #b = playerid[b]
        b=a
        adjmatrixnew[a][b] += 1
    return adjmatrixnew

def playerFind(passingevents):
    a=set(passingevents['OriginPlayerID'])
    b=set(passingevents['DestinationPlayerID'])
    player=list(a|b)
    print(player)
    player=[p.split('_')[1] for p in player]
    playerid=dict()
    for i,p in enumerate(player):
        playerid[p]=i
    return player,playerid

def considerinmatch(matchid):
    fullevents=pd.read_csv(file1+'/'+'passingevents.csv')
    fullevents=fullevents[fullevents['TeamID']=='Huskies']
    fullevents=fullevents[fullevents['MatchID']==matchid]
    fullevents['TimeSpan']=[0 for i in range(len(fullevents))]
    for i in fullevents.index:
        fullevents['TimeSpan'][i]=int(fullevents['EventTime'][i]/900)+1
        if fullevents['MatchPeriod'][i]=='2H':
            fullevents['TimeSpan'][i] += 4

    player,playerid=playerFind(fullevents)
    matrix=[]
    for i in range(1,9):
        line=[i,0]
        data=fullevents[fullevents['TimeSpan']==i]
        #data=data[data['EventType']=='Pass']
        line[1] = TeamPlayeRankget(data)
        matrix.append(line)
    df = pd.DataFrame(matrix, columns=['TimeSpan', 'Team PlayeRank'])
    df.to_csv(file2 + '/' + p2 + '/Team PlayeRank'+str(matchid)+'.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Team PlayeRank', color='g')
    plt.savefig(file3 + '/p2' + '/Team PlayeRank'+str(matchid)+'.png')


def considerallmatch():
    passingevents = pd.read_csv(file1 + '/' + 'passingevents.csv')
    matrix=[]
    for i in range(1,39):
        print(i)
        line=[i,0] #MatchID,maxegi
        data = passingevents[passingevents['MatchID'] == i]
        data = data[data['TeamID'] == 'Huskies']
        #data=data[data['EventType']=='Pass']
        line[1] = TeamPlayeRankget(data)
        matrix.append(line)
    df=pd.DataFrame(matrix,columns=['MatchID','Team PlayeRank'])
    df.to_csv(file2+'/'+p2+'/Team PlayeRank.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='MatchID', y='Team PlayeRank',color='g')
    plt.savefig(file3 + '/p2' + '/Team PlayeRank.png')

def considerallmatchaverage():
    matrix=[[i,0] for i in range(1,9)]#TimeSpan, average_max_eigen
    for i in range(1,39):
        df=pd.read_csv(file2 + '/' + p2 + '/Team PlayeRank'+str(i)+'.csv')
        for j in df.index:
            matrix[j][1]+=df['Team PlayeRank'][j]
    for i in range(8):
        matrix[i][1]/=39
    df=pd.DataFrame(matrix,columns=['TimeSpan','Team PlayeRank'])
    df.to_csv(file2 + '/' + p2 + '/Team PlayeRank_ave.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='Team PlayeRank', color='g')
    plt.savefig(file3 + '/p2' + '/Team PlayeRank_ave.png')


considerallmatch()

for i in range(1,39):
    print(i)
    considerinmatch(i)

considerallmatchaverage()
