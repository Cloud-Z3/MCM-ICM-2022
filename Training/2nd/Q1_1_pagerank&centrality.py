# 比较pagerank和度分布

import numpy as np
import pandas as pd
from scipy.stats import pearsonr,spearmanr
import matplotlib.pyplot as plt

df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']
print(df)

musician=set(df['influencer_name'])|set(df['follower_name'])
musician=list(musician)
print(len(musician))
mu_id=dict()
for i,m in enumerate(musician):
    mu_id[m]=i

n=len(musician)
adj=[[0 for _ in range(n)] for _ in range(n)]

for i in df.index:
    a,b=mu_id[influencer[i]],mu_id[follower[i]]
    adj[a][b]+=1

deg_distr=dict()
rank_distr=dict()

for i in range(n):
    deg_distr[musician[i]]=sum(adj[i])

df_pagerank=pd.read_csv('./Data/p1/4_nodes_pagerank.csv')
for i in df_pagerank.index:
    mu=df_pagerank['Label'][i]
    rank_distr[mu]=df_pagerank['Weight'][i]

points=[]
for item in rank_distr:
    points.append([deg_distr[item],rank_distr[item]])
x,y=zip(*points)
plt.scatter(x,y)
plt.show()
print(pearsonr(x,y))
print(spearmanr(x,y))
print(deg_distr['Bob Dylan'])