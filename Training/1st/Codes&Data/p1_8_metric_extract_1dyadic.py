# Actually, dyadic and triadic configurations are all here.

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

def configurationFind(passingevents):
    player=list(set(passingevents['OriginPlayerID'])|set(passingevents['DestinationPlayerID']))
    player=[p.split('_')[1] for p in player]
    playerid=dict()

    for i,p in enumerate(player):
        playerid[p]=i

    adjmatrixnew=adjget(passingevents,player,playerid)
    ans1=greedyselection2(adjmatrixnew)[0:4]
    ans2=greedyselection3(adjmatrixnew)[0:4]

    '''for a in ans1:
        print(player[a[1][0]], player[a[1][1]],a[0])
        
    for a in ans2:
        print(player[a[1][0]], player[a[1][1]], player[a[1][2]],a[0])'''
    return player,playerid,ans1,ans2

passingevents=pd.read_csv(file1+'/'+'passingevents.csv')
passingevents=passingevents[passingevents['TeamID']=='Huskies']
player,playerid,ans1,ans2=configurationFind(passingevents)

print(ans1)

#二元组
matrix=[]
for i in range(1,39):
    data=passingevents[passingevents['MatchID']==i]
    adj=adjget(data,player,playerid)
    for j in ans1:
        line = [i, 0, 0]
        line[1]='-'.join([player[k] for k in j[1]])
        print(line[1])
        a = j[1][0]
        b = j[1][1]
        line[2] = adj[a][b]
        matrix.append(line)
df2=pd.DataFrame(matrix,columns=['MatchID','Dyadic Configuration','Count'])
df2.to_csv(file2+'/'+p1+'/Dyadic Configuration.csv',index=False)
plt.figure(dpi=600,figsize=(8,5))
sns.lineplot(data=df2,x='MatchID',y='Count',hue='Dyadic Configuration')
plt.savefig(file3+'/p1'+'/Dyadic Configuration.png')

#三元组
matrix=[]
for i in range(1,39):
    data=passingevents[passingevents['MatchID']==i]
    adj=adjget(data,player,playerid)
    for j in ans2:
        line = [i, 0, 0]
        line[1]='-'.join([player[k] for k in j[1]])
        print(line[1])
        a = j[1][0]
        b = j[1][1]
        line[2] = adj[a][b]
        matrix.append(line)
df2=pd.DataFrame(matrix,columns=['MatchID','Triadic Configuration','Count'])
df2.to_csv(file2+'/'+p1+'/Triadic Configuration.csv',index=False)
plt.figure(dpi=600,figsize=(8,5))
sns.lineplot(data=df2,x='MatchID',y='Count',hue='Triadic Configuration')
plt.savefig(file3+'/p1'+'/Triadic Configuration.png')


