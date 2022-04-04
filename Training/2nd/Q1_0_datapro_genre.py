import pandas as pd
from collections import Counter
epsilon=0.1
def distribute_change(nums):
    n = len(nums)
    n_ = len(set(nums))
    nums=[[nums[i],i] for i in range(len(nums))]
    nums.sort()
    num,idx=zip(*nums)
    if n==n_:
        return [epsilon+idx[i]/(n-1)/(1-epsilon) if n!=1 else 1 for i in range(n)]
    else:
        distr=[epsilon + i / (n_ - 1)/(1-epsilon) if n_ != 1 else 1 for i in range(n_)]
        c=Counter(num)
        items=list(set(num))
        items.sort()
        ans=[]
        for i,item in enumerate(items):
            ans.extend([distr[i]]*c[item])
        return [ans[idx[i]] for i in range(n)]

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
influencer_gen=df['influencer_main_genre']
follower_gen=df['follower_main_genre']
print(df)

genre=set(df['influencer_main_genre'])|set(df['follower_main_genre'])
genre=list(genre)
#print(musician)
mu_id=dict()
for i,m in enumerate(genre):
    mu_id[m]=i
print(mu_id)
n=len(genre)
adj=[[0 for _ in range(n)] for _ in range(n)]

for i in df.index:
    a,b=mu_id[influencer_gen[i]],mu_id[follower_gen[i]]
    adj[a][b]+=1
#print(adj)

matrix=[]
for i in range(n):
    for j in range(n):
        if adj[i][j]!=0:
            matrix.append([i,j,adj[i][j]])

# 选择具有影响力的音乐家、深受影响的音乐家
threshold=60
genre_new=set(genre)
for i in range(n):
    if sum(adj[i])<threshold and sum([adj[j][i] for j in range(n)])<threshold:
        genre_new.remove(genre[i])

genre_new=list(genre_new)
n_=len(genre_new)
adj_=[[0 for _ in range(n_)] for _ in range(n_)]
mu_id_=dict()
for i,m in enumerate(genre_new):
    mu_id_[m]=i
for i in df.index:
    if influencer_gen[i] in genre_new and follower_gen[i] in genre_new:
        a,b=mu_id_[influencer_gen[i]],mu_id_[follower_gen[i]]
        adj_[a][b]+=1
print(adj_)

matrix_=[]
Id=0
for i in range(n_):
    for j in range(n_):
        if adj_[i][j]!=0 and i!=j:
            matrix_.append([i,j,'Directed',Id,adj_[i][j]])
            Id+=1

new_weight=distribute_change([matrix_[i][4] for i in range(len(matrix_))])
# print(Counter([matrix_[i][4] for i in range(len(matrix_))]))
for i in range(len(matrix_)):
    matrix_[i][4]=new_weight[i]
df_out=pd.DataFrame(data=matrix_,columns=['Source','Target','Type','Id','Weight'])
df_out.to_csv('./Data/p1/2_network_draw.csv')
# 边

matrix_=[]
sep=qua([sum(adj_[i]) for i in range(n_)])

for i in range(n_):
    weight=sum(adj_[i])
    matrix_.append([i,genre_new[i],weight,allocate(sep,weight)])
new_weight=distribute_change([matrix_[i][2] for i in range(len(matrix_))])
for i in range(len(matrix_)):
    matrix_[i][2]=new_weight[i]
df_out=pd.DataFrame(data=matrix_,columns=['Id','Label','Weight','color'])
# 节点
df_out.to_csv('./Data/p1/3_nodes.csv',index=False)


'''
df_out=pd.DataFrame(data=matrix,columns=['influencer','follower','weight'])
df_out.to_csv('./Data/p1/0_network_draw.csv')
matrix=[]
for i in range(n):
    matrix.append([i,musician[i]])
df_out=pd.DataFrame(data=matrix,columns=['id','musician'])
df_out.to_csv('./Data/p1/1_nodes.csv',index=False)'''