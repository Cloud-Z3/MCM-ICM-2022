# In a single match.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
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
    passingevents['TimeSpan']=[0]*len(passingevents)
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
        eigenvalue, featurevector = np.linalg.eig(adj)
        line[1] = max([abs(i) for i in list(eigenvalue)])
        matrix.append(line)
    df = pd.DataFrame(matrix, columns=['TimeSpan', 'MaxEigenvalue'])
    df.to_csv(file2 + '/' + p1 + '/MaxEigenvalue'+str(matchid)+'.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='MaxEigenvalue', color='g')
    plt.savefig(file3 + '/p1' + '/MaxEigenvalue'+str(matchid)+'.png')


def considerallmatch():
    passingevents = pd.read_csv(file1 + '/' + 'passingevents.csv')
    matrix=[]
    for i in range(1,39):
        print(i)
        line=[i,0] #MatchID,maxegi
        data = passingevents[passingevents['MatchID'] == i]
        data = data[data['TeamID'] == 'Huskies']
        player, playerid = playerFind(data)
        adj=adjget(data, player, playerid)
        #print(adj)
        eigenvalue, featurevector = np.linalg.eig(adj)
        line[1]=max([abs(i) for i in list(eigenvalue)])
        matrix.append(line)
    df=pd.DataFrame(matrix,columns=['MatchID','MaxEigenvalue'])
    df.to_csv(file2+'/'+p1+'/MaxEigenvalue.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='MatchID', y='MaxEigenvalue',color='g')
    plt.savefig(file3 + '/p1' + '/MaxEigenvalue.png')

def considerallmatchaverage():
    matrix=[[i,0] for i in range(1,9)]#TimeSpan, average_max_eigen
    for i in range(1,39):
        df=pd.read_csv(file2 + '/' + p1 + '/MaxEigenvalue'+str(i)+'.csv')
        for j in df.index:
            matrix[j][1]+=df['MaxEigenvalue'][j]
    for i in range(8):
        matrix[i][1]/=39
    df=pd.DataFrame(matrix,columns=['TimeSpan','MaxEigenvalue'])
    df.to_csv(file2 + '/' + p1 + '/MaxEigenvalue_ave.csv')
    plt.figure(dpi=600, figsize=(8, 5))
    sns.lineplot(data=df, x='TimeSpan', y='MaxEigenvalue', color='g')
    plt.savefig(file3 + '/p1' + '/MaxEigenvalue_ave.png')



considerallmatch()

for i in range(1,39):
    considerinmatch(i)

considerallmatchaverage()
