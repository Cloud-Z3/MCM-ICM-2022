from Q2_lib import *

import pandas as pd

df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']
print(df)

musician=set(df['influencer_name'])|set(df['follower_name'])
musician=list(musician)
n=len(musician)

dist_mat=[[0 for _ in range(n)] for _ in range(n)]
matrix=[]
for i in range(n):
    for j in range(n):
        print(i,j)
        if i==j:
            continue
        dist_mat[i][j]=distance_musician(musician[i],musician[j])
        matrix.append([musician[i],musician[j],dist_mat[i][j],1/(1+dist_mat[i][j])])

df_out=pd.DataFrame(data=matrix,columns=['musician1','musician2','distance','similarity'])
df_out.to_csv('./Data/p2/distance_musician.csv')

