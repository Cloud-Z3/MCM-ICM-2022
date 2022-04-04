import pandas as pd
import numpy as np

def zscore(a):
    n=len(a)
    ave=sum(a)/n
    sigma=(sum([(a[i]-ave)**2 for i in range(n)])/n)**0.5
    return [(ai-ave)/sigma for ai in a]

def standard(a):
    maxa = max(a)
    mina = min(a)
    return [(ai - mina) / (maxa - mina) for ai in a]

df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']

musician=[]
for i in df.index:
    if influencer[i] not in musician:
        musician.append(influencer[i])
    if follower[i] not in musician:
        musician.append(follower[i])
n=len(musician)
mu_id=dict()
for i,m in enumerate(musician):
    mu_id[m]=i

adj=[[0 for _ in range(n)] for _ in range(n)]

for i in df.index:
    if influencer[i] in musician and follower[i] in musician:
        a,b=mu_id[influencer[i]],mu_id[follower[i]]
        adj[a][b]+=1
# print(adj)

df_pagerank=pd.read_csv("./data/p1/4_nodes_pagerank.csv")
pagerank=df_pagerank['Weight']
print(pagerank)
pagerank=standard(zscore(pagerank))
print(sum(pagerank)/len(pagerank))

power=[0.670991,0.329009]

misicinfluence=dict()
for i in df_pagerank.index:
    label=df_pagerank['Label'][i]
    misicinfluence[label]=power[0]*pagerank[i]

centrality=[sum(adj[i]) for i in range(n)]
print(centrality)
centrality=standard(zscore(centrality))
print(sum(centrality)/len(centrality))
for i in range(len(adj)):
    item=musician[i]
    misicinfluence[item]+=power[1]*centrality[i]

matrix=[]
for i in range(n):
    matrix.append([i,musician[i],misicinfluence[musician[i]]])
df_out=pd.DataFrame(data=matrix,columns=['Id','Label','Weight'])
df_out.to_csv('./Data/p1/6_music_influence.csv',index=False)

