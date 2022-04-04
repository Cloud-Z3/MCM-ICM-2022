# 计算各节点的pagerank

import numpy as np
import pandas as pd

def qua(nums):
    nums.sort()
    n=len(nums)
    i=n//5
    return [nums[i],nums[i*2],nums[i*3],nums[i*4]]

def allocate(sep,value):
    a,b,c,d=sep
    if value<=a:
        return 'A'
    elif value<=b:
        return 'B'
    elif value<=c:
        return 'C'
    elif value<=d:
        return 'D'
    else:
        return 'E'

df=pd.read_csv("./data/influence_data.csv")
influencer=df['influencer_name']
follower=df['follower_name']
print(df)

musician=set(df['influencer_name'])|set(df['follower_name'])
musician=list(musician)
print(musician)
mu_id=dict()
for i,m in enumerate(musician):
    mu_id[m]=i

n=len(musician)
adj=[[0 for _ in range(n)] for _ in range(n)]

for i in df.index:
    a,b=mu_id[influencer[i]],mu_id[follower[i]]
    adj[a][b]+=1

adj=np.array(adj,dtype=float)
# 邻接矩阵adj至此生成
print(adj)
print(sum(adj))
# adj=adj.transpose()
# 转置
print(sum(adj))
d=0.85
s=sum(adj)
for i in range(n):
    for j in range(n):
        if s[i]!=0:
            adj[j][i]/=s[i]
            # print(adj[j][i])
        else:
            if i==j:
                adj[j][i]=1
            else:
                adj[j][i]=0
# 规范化，使得adj变为随机矩阵（或转移矩阵）
M=adj

inv=np.linalg.inv(np.identity(n,dtype=float)-d*M)
print(inv)
R=np.dot(inv,(1-d)/n*np.array([1 for _ in range(n)]))
# 书上公式
# R=R/sum(R)
print(R[1:100])
print(sum(R))
matrix=[]
sep=qua(R)
#仅为分配颜色需要，不重要
for i in range(n):
    print(musician[i])
    matrix.append([i,musician[i],R[i],allocate(sep,R[i]),'Directed'])
df_out=pd.DataFrame(data=matrix,columns=['Id','Label','Weight','color','Type'])
df_out.to_csv('./Data/p1/4_nodes_pagerank.csv',index=False)